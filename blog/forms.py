from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """ Form for a post """
    class Meta:
        model = Post
        fields = ('title', 'text',)