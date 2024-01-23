from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView
from django.urls import path
from users.views import SignupView, ProfileView, VerifyEmailView, custom_password_reset

app_name = "users"

urlpatterns = [
    path('login/', LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('verify_email/<str:uid>/<str:token>/', VerifyEmailView.as_view(), name='verify_email'),
    path('password_reset/', custom_password_reset, name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
]
