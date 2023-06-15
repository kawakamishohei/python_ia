from django.shortcuts import render
from django.views import generic
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


class TagListView(generic.ListView):
    model = Tag
    template_name = 'blog/tag_list.html'

# class TagListView(generic.ListView):
#     model = Article
#     template_name = 'blog/tag_list.html'
# Create your views here.
