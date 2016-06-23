from django import forms

from .models import Post, Comment
from .choices import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    status = forms.ChoiceField(choices = STATUS_CHOICES, initial='', widget=forms.Select(), required=True)
    relevance = forms.ChoiceField(choices = RELEVANCE_CHOICES, required=True)

    typeCol = forms.ChoiceField(choices = TYPE_CHOICES, label='Type de collectivité')
    class Meta:
        model = Comment
        fields = ('author','text','status','relevance','typeCol')
