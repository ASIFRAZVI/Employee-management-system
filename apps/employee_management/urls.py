from django.urls import path
from apps.employee_management.views.employee import EmployeeView

urlpatterns = [
    path("employee/", EmployeeView.as_view(), name="employee"),
    path("employee/<uuid:id>/", EmployeeView.as_view(), name="employee"),
]
