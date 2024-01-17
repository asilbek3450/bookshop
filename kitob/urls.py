from django.urls import path

from kitob.views import home_page, about, profile_page, book_list, book_detail

urlpatterns = [
    path('', home_page),
    path('about/', about),
    path('profile/', profile_page),

    path('books/', book_list, name='book_list'),
    path('books/<int:pk>', book_detail, name='book_detail'),
]
