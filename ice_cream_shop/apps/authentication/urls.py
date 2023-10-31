from django.urls import path
from django.contrib.auth import views as auth_views

from .views import RegisterUser, LoginUser, logout_user
from .password.password_views import CustomPasswordResetView, CustomPasswordResetConfirmView
from .services.email_manager.email_views import verify_email

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),

    # Email
    path('verify/', verify_email, name='verify_email'),

    # Сброс пароля
    path('password_reset/', CustomPasswordResetView.as_view(template_name='authentication/password/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='authentication/password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(template_name='authentication/password/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='authentication/password/password_reset_complete.html'), name='password_reset_complete'),
]