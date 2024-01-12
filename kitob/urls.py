from django.urls import path

from kitob.views import home_page, about

urlpatterns = [
    path('', home_page),
    path('about/', about)
]
