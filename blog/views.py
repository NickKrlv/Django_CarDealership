from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from django.urls import reverse_lazy


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blogpost_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(View):
    template_name = 'blog/blogpost_detail.html'

    def get(self, request, slug):
        post = get_object_or_404(BlogPost, slug=slug, is_published=True)

        # Увеличиваем счетчик просмотров на 1 при каждом просмотре
        post.views_count += 1
        post.save()

        return render(request, self.template_name, {'post': post})


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/blogpost_form.html'
    fields = ['title', 'content', 'preview', 'is_published']

    def form_valid(self, form):
        form.instance.slug = form.instance.generate_slug()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blogpost_detail', args=[self.object.slug])


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/blogpost_form.html'
    fields = ['title', 'content', 'preview', 'is_published']

    def form_valid(self, form):
        form.instance.slug = form.instance.generate_slug()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blogpost_detail', args=[self.object.slug])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blogpost_confirm_delete.html'
    success_url = reverse_lazy('blogpost_list')
