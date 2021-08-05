from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('logout/', logoutview, name='logout'),
    path('login/', student_login,name="login"),

    path("password_reset/", password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='main/password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="main/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='main/password/password_reset_complete.html'), name='password_reset_complete'),      
]
