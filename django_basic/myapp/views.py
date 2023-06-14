from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


def hello(request):
    return HttpResponse('Hello')


# Create your views here.

def home(request):
    return render(request, 'myapp/home.html')


def home2(request):
    context = {
        'title': 'ホーム2です',
        1: 1,
        'number_list': {1, 2, 3, 4, 5},
    }
    return render(request, 'myapp/home2.html', context)


class Home(generic.TemplateView):
    template_name = 'myapp/home2.html'

    # テンプレートファイルに、追加で渡したいデータがあるときは
    # このメソッドを呼ぶ
    def get_context_data(self, **kwargs):
        # このメソッド上書きのときは、毎回super()で親のメソッドを呼ぶこと
        context = super().get_context_data(**kwargs)
        context['title'] = 'ホーム2です'
        return context
