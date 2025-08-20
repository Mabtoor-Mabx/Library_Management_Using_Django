from django.shortcuts import render, redirect
from .models import Book, Author
from .forms import BookForm

# Create your views here.

# Show List of Author and Books
def author_list(request):
    authors = Author.objects.all()
    return render(request, "author_list.html", {'authors': authors})

# Add a New Book (With Relation to Author)

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = BookForm()
    return render(request, "add_book.html", {'form': form})