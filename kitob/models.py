from django.db import models


# Create your models here.
class Book(models.Model):
    nomi = models.CharField(max_length=100, null=False)
    muallif = models.CharField(max_length=50)
    janri = models.CharField(max_length=100)
    publication_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.nomi
