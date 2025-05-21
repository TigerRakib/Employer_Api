from django.urls import path
from .views import EmployerList,EmployerDetails

urlpatterns = [
    path('', EmployerList.as_view()),
    path('<int:pk>/', EmployerDetails.as_view()),
    
]
