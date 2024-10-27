from django.urls import path
from apps.base.views.base import Welcome

urlpatterns = [path("", Welcome.as_view(), name="welcome")]
