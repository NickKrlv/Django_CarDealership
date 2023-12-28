from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog_previews/', verbose_name='Превью', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Блоговая запись'
        verbose_name_plural = 'Блоговые записи'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Генерация slug из заголовка
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
