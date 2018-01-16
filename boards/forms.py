from django import forms
from .models import Topic
from .models import Post


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 5, 'placeholder': '表达你的想法！'}
    ), max_length=500, help_text='最多输入500字')

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]