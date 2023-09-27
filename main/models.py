from django.db import models
from django.contrib.auth.models import User

class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    level = models.IntegerField()
    # Atribut lain yang relevan dengan karakter

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    owner = models.ForeignKey(Character, on_delete=models.CASCADE, default=None, null=True)  # Menambahkan relasi dengan Character

    #Atribut lain yang relevan dengan item

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)