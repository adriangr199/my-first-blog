from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','text')
"""
class LangForm(forms.ModelForm):
    class Meta:
    	model=Lang
    	fields=['language']
"""