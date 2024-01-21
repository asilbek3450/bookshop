from django.forms import ModelForm

from kitob.models import Book


class BookCreateForm(ModelForm):

    class Meta:
        model = Book
        fields = ['nomi', 'information', 'muallif', 'rasm', 'narxi', 'janri']


class BookEditForm(ModelForm):
    class Meta:
        model = Book
        fields = ['nomi', 'information', 'narxi', 'rasm', 'narxi', 'janri']
