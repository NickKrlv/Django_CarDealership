
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserSignupForm
from users.models import User


class SignupView(CreateView):
    model = User
    form_class = UserSignupForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'
