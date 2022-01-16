from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=21)
    last_name = models.CharField(max_length=28)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'