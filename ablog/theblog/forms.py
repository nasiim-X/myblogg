from django import forms 
from .models import Post, Category

#catgry = [('Coding','Coding'),('Sports','Sports'),('Entertainment','Entertainment'),('Travelling & Guides','Travelling & Guides')]
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('title', 'title_tag', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add a Title tag'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Author'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': 'Select Category'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your post here...'}),
        }




class EditForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title placeholder'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add a Title tag'}),
            #'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Author'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your post here...'}),
        }