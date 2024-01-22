from django.urls import path

from kitob.views import home_page, about, profile_page, book_list, book_detail, create_book, edit_book, delete_book

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about),
    path('profile/', profile_page),

    path('books/', book_list, name='book_list'),
    path('books/<int:pk>', book_detail, name='book_detail'),

    path('create/', create_book, name='create_book'),
    path('edit/<int:pk>', edit_book, name='edit_book'),

    path('delete/<int:pk>', delete_book, name='kitob_ochirish')
]
