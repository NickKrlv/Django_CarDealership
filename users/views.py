import random
import string

from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView
from users.forms import UserSignupForm, UserProfileForm
from users.models import User


class SignupView(CreateView):
    model = User
    form_class = UserSignupForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        new_user = form.save()
        token = ''.join(random.choices(string.ascii_letters + string.digits, k=50))
        new_user.verification_token = token
        new_user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'Подтвердите ваш аккаунт'
        message = (
            f'Поздравляем, Вы зарегистрировались на нашем портале!\n'
            f'Для завершения регистрации и подтверждения вашей электронной почты, '
            f'пожалуйста, кликните по следующей ссылке:\n'
            f'http://{current_site.domain}{reverse("users:verify_email", kwargs={"uid": new_user.pk, "token": token})}'
        )
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email])
        return super().form_valid(form)


class VerifyEmailView(View):
    def get(self, request, uid, token):
        try:
            user = User.objects.get(pk=uid, verification_token=token)
            user.is_active = True
            user.save()
            return render(request, 'users/registration_success.html')
        except User.DoesNotExist:
            return render(request, 'users/registration_failed.html')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def custom_password_reset(request, *args, **kwargs):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return HttpResponseNotFound('Пользователь не найден')

        new_password = User.objects.make_random_password()
        user.set_password(new_password)
        user.save()

        current_site = get_current_site(request)
        message = (
            f'Ваш новый пароль: {new_password}\n'
            f'Пожалуйста, войдите в свою учетную запись с новым паролем.'
            f'http://{current_site.domain}{reverse("users:login")}'
        )
        send_mail(
            subject='Новый пароль',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )

        return HttpResponse('<h1 class="text-center">Новый пароль выслан на почту</h1>')

    form = PasswordResetForm()
    return render(request, 'users/password_reset_form.html', {'form': form})
