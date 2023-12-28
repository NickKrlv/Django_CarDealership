from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import BlogPost


@receiver(post_save, sender=BlogPost)
def send_congratulations_email(sender, instance, **kwargs):
    if instance.views_count == 100:
        subject = 'Поздравляем с достижением 100 просмотров!'
        message = f'Статья "{instance.title}" достигла 100 просмотров! Поздравляем!'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.YOUR_EMAIL_ADDRESS]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
