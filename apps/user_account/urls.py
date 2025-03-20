from django.urls import path 
from .views import *
from django.contrib.auth.views import PasswordResetDoneView

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('registration/',Registration.as_view(),name='registration'),
    path('change-password/',ChangePassword.as_view(),name='change-password'),

    path('password_reset/', SendEmailToResetPassword.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', ResetPasswordConfirm.as_view(), name='password_reset_confirm'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='user_account/password-reset-done.html'), name='password_reset_done'),
]
