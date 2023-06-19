from django import forms

from .models import Tag, Article


class TagCreateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'text', 'created_at', 'category', 'tags',)


class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'text', 'created_at', 'category', 'tags',)
