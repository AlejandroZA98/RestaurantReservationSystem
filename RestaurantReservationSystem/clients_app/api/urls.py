from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path 
from clients_app.api.views.registration_view import RegisterUser
from clients_app.api.views.logout_view import LogoutUser

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView# type: ignore importacion de JWT
urlpatterns =[
    path('register/',RegisterUser.as_view(),name='register'),#registrar usuario
    path('logout/',LogoutUser.as_view(),name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),#generar tokens con JWT(puede ser usado como login)
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),#renovar token_refresh
]