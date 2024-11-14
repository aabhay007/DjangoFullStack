# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('book_list')  # Redirect to book list on successful login
        else:
            return HttpResponse('Invalid username or password.')  # Handle incorrect credentials
    return render(request, 'myapp/login.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logging out

# Signup view
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Create a new user
            return redirect('login')  # Redirect to login page on successful signup
    else:
        form = UserCreationForm()
    return render(request, 'myapp/signup.html', {'form': form})

@login_required
# Read - List all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books': books})

# Read - Display details of a single book
def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'myapp/book_detail.html', {'book': book})

# Create - Add a new book
def book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')
        Book.objects.create(title=title, author=author, published_date=published_date)
        return redirect('book_list')
    return render(request, 'myapp/book_form.html')

# Update - Edit an existing book
def book_update(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.published_date = request.POST.get('published_date')  
        book.save()
        return redirect('book_list')
    book.published_date = book.published_date.strftime('%Y-%m-%d')

    return render(request, 'myapp/book_form.html', {'book': book})

# Delete - Remove a book
def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'myapp/book_confirm_delete.html', {'book': book})
