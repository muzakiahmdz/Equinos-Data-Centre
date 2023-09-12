from django.shortcuts import render
from .models import Character, Item

def character_list(request):
    characters = Character.objects.all()
    return render(request, 'main/character_list.html', {'characters': characters})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'main/item_list.html', {'items': items})

def show_main(request):
    context = {
        'name': 'Muzaki Ahmad Ridho Azizy',
        'app_name': 'Equinos',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
# Create your views here.
