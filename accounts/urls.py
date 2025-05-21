from django.urls import path
from .views import SignUpView,LoginView,ProfileView

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('profileview/', ProfileView.as_view()),
    
]
