from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import NewsForm
from .models import *
from .filters import PostFilter


class PostList(ListView):
    model = Post
    ordering = 'text'
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs


class PostSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search'
    filter_class = PostFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_news',)
    raise_exception = True
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        form.instance.categoryType = 'NW'
        return super().form_valid(form)


class NewsEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.update_news',)
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        form.instance.categoryType = 'NW'
        return super().form_valid(form)


class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_news',)
    form_class = NewsForm
    model = Post
    template_name = 'news_delete.html'

    def form_valid(self, form):
        form.instance.categoryType = 'NW'
        return super().form_valid(form)


class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_article',)
    form_class = NewsForm
    model = Post
    template_name = 'articles_edit.html'

    def form_valid(self, form):
        form.instance.categoryType = 'AR'
        return super().form_valid(form)


class ArticleEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.update_article',)
    form_class = NewsForm
    model = Post
    template_name = 'articles_edit.html'

    def form_valid(self, form):
        form.instance.categoryType = 'AR'
        return super().form_valid(form)


class ArticleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_article',)
    form_class = NewsForm
    model = Post
    template_name = 'articles_delete.html'

    def form_valid(self, form):
        form.instance.categoryType = 'AR'
        return super().form_valid(form)