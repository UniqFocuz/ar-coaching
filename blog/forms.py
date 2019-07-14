from django.forms import ModelForm
from .models import Post, Announcement

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=['title','content']

class AnnouncementForm(ModelForm):
    class Meta:
        model=Announcement
        fields=['announcement']