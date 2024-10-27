from rest_framework import serializers
from apps.authentication.models.user_auth import CustomUser
from apps.employee_management.models.employee import Employee


class EmployeeCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email"]


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = ["id", "name", "email", "department", "role", "user"]
