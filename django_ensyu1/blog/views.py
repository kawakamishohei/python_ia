from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect
from .forms import TagCreateForm, ArticleCreateForm,ArticleUpdateForm,SearchForm,CommentCreateForm
from .models import Article, Tag,Comment


class Home(generic.TemplateView):
    template_name = 'blog/home.html'


class ArticleListView(generic.ListView):
    model = Article
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # フォーム(request.GETやrequest.POST)とすると、
        # このフォームをテンプレートで表示すると、入力済みになっている
        context['form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = SearchForm(self.request.GET)
        form.is_valid()
        keyword = form.cleaned_data.get('keyword')
        if keyword:
            #記事タイトルか本文のどちらかにキーワードが含まれていれば表示
            queryset = queryset.filter(Q(title__icontains=keyword) | Q(text__icontains=keyword))
        return queryset

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


class ArticleUpdate(generic.UpdateView):
    model = Article
    form_class = ArticleUpdateForm
    template_name = 'blog/article_update.html'
    success_url = reverse_lazy('blog:article_list')

class ArticleDelete(generic.DeleteView):
    model = Article
    template_name = 'blog/article_delete.html'
    success_url = reverse_lazy('blog:article_list')

class CommentCreateView(generic.CreateView):
    model = Comment
    template_name = 'blog/comment_create.html'
    success_url = reverse_lazy('blog:article_list')
    form_class = CommentCreateForm

    def form_valid(self, form):
        # form.save(commit=False) データベースにはまだ保存しない
        # commit=Falseビューで、モデルのフィールドを埋めるために使う引数
        comment = form.save(commit=False)

        # Commentモデルの、targetフィールドをここで埋める
        # モデル名.objects.get(フィールド=値)  1つだけ、DBから取り出すのに使うのがget
        # url内の<int:pk>は、self.kwargs['pk'] で取得できる
        comment.target = Article.objects.get(pk=self.kwargs['pk'])

        comment.save()  # saveしないと保存されない
        return redirect('blog:article_list')

