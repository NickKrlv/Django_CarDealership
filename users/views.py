from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView
from users.forms import UserSignupForm, UserProfileForm
from users.models import User
from users.utils import send_verification_email


class SignupView(CreateView):
    model = User
    form_class = UserSignupForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
