# Import Libraries
from django import forms
from .models import Book

# Form for adding New Book (Modelform)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
