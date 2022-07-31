from dataclasses import field, fields
from pyexpat import model
from .models import Post , Comment
from django import forms 


class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':2 , 'placeholder':'Post...'}))
    class Meta:
        model = Post
        fields = ('title','content')


# we are not picking date created , bc is auto, and creator is by default the user
# we can now use the form inside our views 


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content',)
        
class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Comment...'}))
    class Meta:
        model=Comment
        fields = ('content',)