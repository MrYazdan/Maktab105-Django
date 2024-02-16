from django import forms
from .models import Post, User
from tinymce.widgets import TinyMCE


# class PostForm(forms.Form):
#     title = forms.CharField(max_length=105,
#                             help_text="this is title of posts, take attention for choose correct title ^_-")
#     content = forms.Field(widget=TinyMCE(attrs={'rows': 2}))
#     is_active = forms.BooleanField()
#     author = forms.ModelChoiceField(queryset=User.objects.all(), required=True)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = "__all__"
        fields = ['title', 'author', 'content']
