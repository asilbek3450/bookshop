from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from kitob.forms import BookCreateForm, BookEditForm
from kitob.models import Book


# Create your views here.
def home_page(request):
    return HttpResponse("Salom, dunyo")


def about(request):
    return HttpResponse("About sahifasi")


def profile_page(request):
    return HttpResponse("Assalomu aleykum Asilbek aka")


def book_list(request):
    books = Book.objects.all()
    context = {
        'kitoblar': books
    }
    return render(request, template_name='book_list.html', context=context)


def book_detail(request, pk):
    # book = Book.objects.get(pk=pk)
    book = get_object_or_404(Book, pk=pk)
    context = {
        'kitob': book
    }
    return render(request, template_name='book_detail.html', context=context)


def create_book(request):
    if request.method == 'POST':
        form = BookCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookCreateForm()
    context = {
        'form': form
    }
    return render(request, 'book_create.html', context=context)


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', pk=book.id)
    else:
        form = BookEditForm(instance=book)
    context = {
        'kerakli_kitob': book,
        'form': form
    }
    return render(request, template_name='book_edit.html', context=context)


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')
