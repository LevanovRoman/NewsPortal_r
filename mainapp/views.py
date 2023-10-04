from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import *
from .forms import *
from .filters import PostFilter

menu = [
    {'title': 'Главная', 'url_name': 'main'},
    {'title': 'Новости', 'url_name': 'show_all_news'},
    {'title': 'Статьи', 'url_name': 'show_all_articles'},
]


class MainPage(ListView):
    model = Post
    template_name = 'mainapp/base.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная'
        return context


class ShowAllNews(ListView):
    model = Post
    template_name = 'mainapp/show-all-posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        queryset = Post.objects.filter(type='Nv').order_by('-time_created')
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.groups.filter(name='authors').exists():
            context['menu'] = menu + [
                {'title': 'Создать новость', 'url_name': 'create_news'}]
        else:
            context['menu'] = menu
        context['title'] = 'Новости'
        context['filterset'] = self.filterset
        context['is_author'] = self.request.user.groups.filter(name='authors').exists()
        return context


class ShowAllArticles(ListView):
    model = Post
    template_name = 'mainapp/show-all-posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.groups.filter(name='authors').exists():
            context['menu'] = menu + [
                {'title': 'Создать статью', 'url_name': 'create_articles'}]
        else:
            context['menu'] = menu
        context['title'] = 'Статьи'
        context['filterset'] = self.filterset
        context['is_author'] = self.request.user.groups.filter(name='authors').exists()
        return context

    def get_queryset(self):
        queryset = Post.objects.filter(type='St').order_by('-time_created')
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs


class ShowPost(DetailView):
    model = Post
    template_name = 'mainapp/post-page.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Новость'
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('post', kwargs={'post_slug': self.get_object().slug})


class Category(ListView):
    model = Category
    template_name = 'mainapp/post-page.html'


class CreateNews(PermissionRequiredMixin, CreateView):
    permission_required = ('mainapp.add_post',)
    form_class = NewsForm
    model = Post
    template_name = 'mainapp/post-create.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['type'] = 'Добавить новость'
        context['title'] = 'Добавление новости'
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = "Nv"
        return super().form_valid(form)


class CreateArticles(PermissionRequiredMixin, CreateView):
    permission_required = ('mainapp.add_post',)
    form_class = NewsForm
    model = Post
    template_name = 'mainapp/post-create.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['type'] = 'Добавить статью'
        context['title'] = 'Добавление статьи'
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = "St"
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('mainapp.change_post',)
    model = Post
    fields = ('author', 'title', 'text', 'category')
    template_name = 'mainapp/post-update.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('post', kwargs={'post_slug': self.get_object().slug})

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['type'] = 'Изменить статью'
        context['title'] = 'Изменение статьи'
        return context


class DeletePost(PermissionRequiredMixin, DeleteView):
    permission_required = ('mainapp.delete_post',)
    model = Post
    template_name = 'mainapp/post-delete.html'
    success_url = reverse_lazy('main')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['type'] = 'Удалить статью'
        context['title'] = 'Удаление статьи'
        return context


@login_required
def get_author(request):
    user = request.user
    author_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        author_group.user_set.add(user)
    return redirect('/')
