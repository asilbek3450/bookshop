from django import forms
from django.forms import ModelForm

from kitob.models import Book, ContactUs


class BookCreateForm(ModelForm):
    class Meta:
        model = Book
        fields = ['nomi', 'information', 'muallif', 'rasm', 'narxi', 'janri']


class BookEditForm(ModelForm):
    class Meta:
        model = Book
        fields = ['nomi', 'information', 'narxi', 'rasm', 'narxi', 'janri']
        widgets = {
            'nomi': forms.TextInput(attrs={'class': 'form-control'}),
            'information': forms.Textarea(attrs={'class': 'form-control'}),
            'narxi': forms.NumberInput(attrs={'class': 'form-control'}),
            'rasm': forms.FileInput(attrs={'class': 'form-control'}),
            'janri': forms.Select(attrs={'class': 'form-control'}),
        }


class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'subject', 'message']

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingizni kiriting...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Emailingizni kiriting...'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mavzu...'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Xabaringizni kiriting...', 'rows': 4}),
        }
