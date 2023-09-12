from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=255)
    level = models.IntegerField()
    # Atribut lain yang relevan dengan karakter

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    # Atribut lain yang relevan dengan item
