from django import forms
from .models import Posts
from django.core.exceptions import ValidationError

class PostsForm(forms.ModelForm):
   class Meta:
       model = Posts
       fields = [
           'name_post',
           'text_post',
           'rating',
           'posts',
           'postCategory',
       ]

   def clean(self):
       cleaned_data = super().clean()
       text_post = cleaned_data.get("text_post")
       if text_post is not None and len(text_post) < 20:
           raise ValidationError({
               "text_post": "Текст статьи не может быть менее 20 символов."
           })

       name_post = cleaned_data.get("name_post")
       if name_post == text_post:
           raise ValidationError(
               "Текст статьи не должен быть идентичен названию."
           )

       return cleaned_data