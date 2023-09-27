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
    class Meta:
        model = Item
        fields = ['name', 'amount', 'description', 'owner']
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ItemForm, self).__init__(*args, **kwargs)
        
        # Filter queryset karakter berdasarkan pengguna saat ini
        if user:
            self.fields['owner'].queryset = Character.objects.filter(user=user)

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]