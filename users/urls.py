from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import SignupView

app_name = "users"

urlpatterns = [
    path('', LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('signup/', SignupView.as_view(), name="signup"),
]
