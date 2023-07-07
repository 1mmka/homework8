from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=64)
    location = models.TextField()

    date_of_open = models.DateField()
    # добавил и сделал миграцию отдельно для app1

    def __str__(self):
        return self.name