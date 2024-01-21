from django.db import models


# Create your models here.
class Book(models.Model):
    nomi = models.CharField(max_length=100, null=False)
    information = models.TextField(null=True, blank=True)
    muallif = models.CharField(max_length=50)
    rasm = models.ImageField(upload_to='kitob_rasmlari/'    )
    narxi = models.DecimalField(max_digits=10, decimal_places=2)

    janri = models.CharField(max_length=100)
    publication_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.nomi
