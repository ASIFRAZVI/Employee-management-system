from django.db import models
from apps.base.models.base import BaseModel
from apps.employee_management import utils
from apps.authentication.models.user_auth import CustomUser


class Employee(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    department = models.CharField(choices=utils.DEPARTMENT_CHOICES, null=True)
    role = models.CharField(choices=utils.ROLE_CHOICES, null=True)

    class Meta:
        db_table = "employee_master"
