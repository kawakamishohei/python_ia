from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import TagCreateForm, ArticleCreateForm
from .models import Article, Tag


class Home(generic.TemplateView):
    template_name = 'blog/home.html'


class ArticleListView(generic.ListView):
    model = Article
    template_name = 'blog/article_list.html'


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'blog/article_detail.html'

    def get_object(self, queryset=None):
        # self.kwargsは、URL内の int:pkといった部分が入っている
        article = Article.objects.get(pk=self.kwargs['pk'])
        # →Staff.objects.get(pk=1)  # 今回、URLは/staff_detail/1/
        # →Staff.objects.get(id=1)  # pkというのは、primarykeyのこと。今回ならidフィールドのこと
        return article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        context['tags'] = article.tags.all()
        return context


class TagListView(generic.ListView):
    model = Tag
    template_name = 'blog/tag_list.html'


# class TagListView(generic.ListView):
#     model = Article
#     template_name = 'blog/tag_list.html'
# Create your views here.

class TagCreateView(generic.CreateView):
    model = Tag
    template_name = 'blog/tag_create.html'
    success_url = reverse_lazy('blog:article_list')
    form_class = TagCreateForm


class ArticleCreateView(generic.CreateView):
    model = Article
    template_name = 'blog/article_create.html'
    success_url = reverse_lazy('blog:article_list')
    form_class = ArticleCreateForm
