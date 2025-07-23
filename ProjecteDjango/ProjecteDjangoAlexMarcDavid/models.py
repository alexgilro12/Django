from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Platform(models.Model):
    name = models.CharField(max_length=100)
    data_de_creacio = models.DateField()
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.TextField(max_length=200)
    price = models.IntegerField()
    new = models.BooleanField()
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

