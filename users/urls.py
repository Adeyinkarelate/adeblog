from unicodedata import name
from django.urls import path 
from .views import sing_up , profile
from django.contrib.auth import views 
# nb: if a view already exit, to avoid conflict , u can import it as e.g views as auth_view

urlpatterns = [
    path('sing_up/', sing_up, name='user-sing_up'),
    path('', views.LoginView.as_view(template_name='users/login.html'), name="user-login"),
    path('logout/', views.LogoutView.as_view(template_name='users/logout.html'), name="user-logout"),
    path('profile/', profile, name='user-profile'),
    path('password_reset/',views.PasswordResetView.as_view(template_name='users/password_reset.html'), name="password-reset"),
    path('password_reset_done/',views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name="password_reset_confirm"),
    path('password_reset_complete/',views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name="password_reset_complete"),
]


 