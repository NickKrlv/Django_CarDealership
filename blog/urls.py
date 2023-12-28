from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView

urlpatterns = [
    path('blogpost_list/', BlogPostListView.as_view(), name='blogpost_list'),
    path('create/', BlogPostCreateView.as_view(), name='blogpost_create'),
    path('<slug:slug>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('<slug:slug>/update/', BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('<slug:slug>/delete/', BlogPostDeleteView.as_view(), name='blogpost_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
