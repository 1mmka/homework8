from django.db import models

# Create your models here.
class Author(models.Model):
    fname = models.CharField(max_length=64)
    lname = models.CharField(max_length=64)
    date_of_birth = models.DateField()

    date_of_death = models.DateField()
    # добавил и сделал общую миграцию
    def __str__(self):
        return self.fname