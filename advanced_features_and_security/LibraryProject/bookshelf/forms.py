from django.shortcuts import redirect, render, get_object_or_404
from .models import Book
from .forms import BookForm

# Secure way to handle book searches using Django ORM
def search_books(request):
    query = request.GET.get('q', '')
    if query:
        books = Book.objects.filter(title__icontains=query)  # Prevents SQL injection by using ORM
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Form submission view with input validation
def submit_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():  # Validates data
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})