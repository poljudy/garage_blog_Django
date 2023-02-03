from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    """
    Create a form where user can upload the detail of the car
    """
    class Meta:
        """
        These are the available fields for post
        """
        model = Post
        fields = (
            'title',
            'slug',
            'author',
            'featured_image',
            'excerpt',
            'content',
            'status',
            'likes',
        )

        def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
