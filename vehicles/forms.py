from django import forms
from .models import Comment, Post, Vehicle, SparePart


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


class VehicleForm(forms.ModelForm):
    """
    Create a form where user can upload the detail of the Vehicle
    """
    required_css_class = 'required-field'
    error_css_class = 'error-field'

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
            'youtube_link'
        )

        def __init__(self, *args, **kwargs):
            super(PostVehicle, self).__init__(*args, **kwargs)


class SparePartForm(forms.ModelForm):
    required_css_class = 'required-field'
    error_css_class = 'error-field'

    class Meta:
        model = SparePart
        fields = [
            'sparepartname',
            'brand',
            'quantity'
        ]


class PostVehicleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
