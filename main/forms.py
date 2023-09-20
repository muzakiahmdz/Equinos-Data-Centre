from django.forms import ModelForm
from main.models import Product
from django import forms
from .models import Character, Item

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'level']

from django.forms import ModelChoiceField

class ItemForm(forms.ModelForm):
    owner = ModelChoiceField(queryset=Character.objects.all(), empty_label="Pilih Karakter")
    class Meta:
        model = Item
        fields = ['name', 'amount', 'description', 'owner']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]