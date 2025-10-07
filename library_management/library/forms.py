from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Book



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn','image']
