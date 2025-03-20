from django.urls import path 
from .views import *

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('registration/',Registration.as_view(),name='registration'),
    path('change-password/',ChangePassword.as_view(),name='change-password'),
]
