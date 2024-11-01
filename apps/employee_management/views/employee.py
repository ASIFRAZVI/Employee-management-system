from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.employee_management.models.employee import Employee
from apps.employee_management.serializers.employee_serializers import (
    EmployeeCreatorSerializer,
    EmployeeSerializer,
)
from apps.base.serializers.base import UUIDFeildSerializer
from rest_framework import permissions
from apps.authentication.jwt_processor.jwt_decoder import decode_jwt_token
from apps.base.helpers.get_element import getObject
from rest_framework.pagination import PageNumberPagination

class EmployeePagination(PageNumberPagination):
    page_size = 3 


class EmployeeView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [decode_jwt_token]

    def post(self, request, *args, **kwargs):
        """This method responsible for creation Employees"""
        data = request.data
        data["user"] = request.user.id

        employee_serializer = EmployeeCreatorSerializer(data=data)
        if not employee_serializer.is_valid():
            return Response({"error": employee_serializer.errors}, status=400)

        validated_data = employee_serializer.validated_data
        validated_email = validated_data["email"]
        validated_user = request.user.id

        employee_email_obj = Employee.objects.filter(
            email=validated_email, user__id=validated_user
        )
        if employee_email_obj.exists():
            return Response({"error": "Please provide Unique Email"})

        employee_serializer.save()
        return Response({"message": "Employee Added!"})

    def get(self, request, id=None, *args, **kwargs):
        """This method responsible for listing and retreiving Employees"""
        user = request.user.id

        if id is None:
            employee_obj = Employee.objects.filter(user__id=user)

            paginator = EmployeePagination()
            paginated_employees = paginator.paginate_queryset(employee_obj, request)
            employee_serializer = EmployeeSerializer(paginated_employees, many=True)
            return paginator.get_paginated_response(employee_serializer.data)
            # employee_serializer = EmployeeSerializer(employee_obj, many=True)
            # return Response(employee_serializer.data, status=200)

        id_serializer = UUIDFeildSerializer(data={"id": id})
        if not id_serializer.is_valid():
            return Response({"error": "Please provide valid Employee id"}, status=400)

        employee_object = getObject(Employee, id)
        if employee_object is None:
            return Response(
                {"error": "provided employee id doesn't exists"}, status=400
            )

        employee_serializers = EmployeeSerializer(employee_object)
        return Response(employee_serializers.data, status=200)

    def put(self, request, id=None, *args, **kwargs):
        """This method responsible for Updating Employees"""
        user = request.user.id

        if id is None:
            return Response({"error": "please provide Employee id "}, status=400)

        id_serializer = UUIDFeildSerializer(data={"id": id})
        if not id_serializer.is_valid():
            return Response({"error": "invalid employee uuid"}, status=400)

        employee_obj = getObject(Employee, id)

        if employee_obj is None:
            return Response(
                {"error": "provided employee id doesn't exists"}, status=400
            )

        data = request.data
        data["user"] = request.user.id
        employee_serializer = EmployeeCreatorSerializer(employee_obj, data)

        if not employee_serializer.is_valid():
            return Response(employee_serializer.errors, status=400)

        employee_serializer.save()
        return Response({"message": "Employee details updated!"})

    def delete(self, request, id=None, *args, **kwargs):
        """This method responsible for deleting employees"""
        if id is None:
            return Response({"error": "please provide Employee id "}, status=400)

        employee_obj = getObject(Employee, id)

        if employee_obj is None:
            return Response({"error": "entered employee id doesn't exists"})
        employee_obj.delete()

        return Response({"message": "employee deleted!"}, status=204)
