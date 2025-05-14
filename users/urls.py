from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import *


app_name = 'users'

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('user/<int:user_id>/', AccountDetailAPIView.as_view(), name='user-account'),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]