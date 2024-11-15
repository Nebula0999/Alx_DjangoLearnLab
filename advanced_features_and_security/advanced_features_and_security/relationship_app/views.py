from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
#from .forms import BookForm

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


# Class-based view for displaying library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'



# Custom view for user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after successful registration
            return redirect('list_books')  # Redirect to a suitable page (e.g., list_books)
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# Helper function to check user roles
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Admin-only view
@user_passes_test(is_admin)
@login_required
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian-only view
@user_passes_test(is_librarian)
@login_required
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member-only view
@user_passes_test(is_member)
@login_required
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

# View to edit a book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

# View to delete a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})