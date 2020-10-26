from django import forms

from .models import Writing, Comment


class WritingForm(forms.ModelForm):
    class Meta:
        model = Writing
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {
            'title': '제목',
            'content': '내용',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control col'}),
        }
        labels = {
            'content': '댓글',
        }
