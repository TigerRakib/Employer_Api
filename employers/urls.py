from django.urls import path
from .views import EmployerList

urlpatterns = [
    path('', EmployerList.as_view()),
]
