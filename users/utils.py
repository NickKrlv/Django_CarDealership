from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes


def send_verification_email(user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)

    verification_url = f"http://your_domain.com/verify-email/{uid}/{token}/"

    subject = 'Подтверждение email'
    message = f'Пройдите по ссылке для подтверждения email: {verification_url}'

    user.email_user(subject, message)
