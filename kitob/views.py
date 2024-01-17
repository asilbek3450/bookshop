from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

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
