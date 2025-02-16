from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import LoginView, UserRegistrationView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
