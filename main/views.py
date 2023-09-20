from django.shortcuts import render, get_object_or_404
from .models import Character, Item
from .forms import CharacterForm, ItemForm
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from main.models import Product
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import xml.etree.ElementTree as ET



def character_list(request):
    characters = Character.objects.all()
    return render(request, 'main/character_list.html', {'characters': characters})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'main/item_list.html', {'items': items})

def show_main(request):
    products = Product.objects.all()
    characters = Character.objects.all()
    items = Item.objects.all()
    jumlah_character = len(characters)  # Menghitung jumlah karakter
    jumlah_item = len(items)  # Menghitung jumlah item

    context = {
        'name': 'Muzaki Ahmad Ridho Azizy', # Nama kamu
        'class': 'PBP B', # Kelas PBP kamu
        'app_name': 'Equinos',
        'products': products,
        'characters': characters,
        'items': items,
        'jumlah_character': jumlah_character,  # Sertakan jumlah karakter dalam konteks
        'jumlah_item': jumlah_item, 
    }

    return render(request, "main.html", context)


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    characters = Character.objects.all()
    items = Item.objects.all()

    # Menggabungkan daftar karakter dan daftar item
    data = list(characters) + list(items)

    # Mengonversi data menjadi XML
    xml_data = serializers.serialize("xml", data)

    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    characters = Character.objects.all()
    items = Item.objects.all()

    # Menggabungkan daftar karakter dan daftar item
    data = list(characters) + list(items)

    # Mengonversi data menjadi JSON
    json_data = serializers.serialize("json", data)

    return JsonResponse(json_data, safe=False)

def show_character_by_id_xml(request, id):
    character = get_object_or_404(Character, pk=id)
    
    # Membuat elemen XML untuk karakter
    character_element = ET.Element("Character")
    ET.SubElement(character_element, "Name").text = character.name
    ET.SubElement(character_element, "Level").text = str(character.level)
    
    # Membuat respons HTTP dengan konten tipe XML
    response = HttpResponse(content_type='application/xml')
    
    # Mengonversi elemen XML menjadi string dan menambahkannya ke respons
    character_tree = ET.ElementTree(character_element)
    character_tree.write(response, encoding='utf-8')
    
    return response

def show_item_by_id_xml(request, id):
    item = get_object_or_404(Item, pk=id)
    
    # Membuat elemen XML untuk item
    item_element = ET.Element("Item")
    ET.SubElement(item_element, "Name").text = item.name
    ET.SubElement(item_element, "Amount").text = str(item.amount)
    ET.SubElement(item_element, "Description").text = item.description
    
    # Jika item memiliki pemilik (owner), tambahkan informasi pemilik
    if item.owner:
        owner_element = ET.SubElement(item_element, "Owner")
        ET.SubElement(owner_element, "Name").text = item.owner.name
    
    # Membuat respons HTTP dengan konten tipe XML
    response = HttpResponse(content_type='application/xml')
    
    # Mengonversi elemen XML menjadi string dan menambahkannya ke respons
    item_tree = ET.ElementTree(item_element)
    item_tree.write(response, encoding='utf-8')
    
    return response

def show_character_by_id(request, id):
    character = get_object_or_404(Character, pk=id)
    # Mengonversi objek karakter menjadi JSON
    json_data = serializers.serialize("json", [character])
    return JsonResponse(json_data, safe=False)

def show_item_by_id(request, id):
    item = get_object_or_404(Item, pk=id)
    # Mengonversi objek item menjadi JSON
    json_data = serializers.serialize("json", [item])
    return JsonResponse(json_data, safe=False)

def create_character(request):
    character_form = CharacterForm(request.POST or None)

    if character_form.is_valid() and request.method == "POST":
        character_form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    characters = Character.objects.all()  # Menambahkan definisi characters
    context = {'character_form': character_form, 'characters': characters}  # Mengirim characters ke dalam konteks
    return render(request, "char_list.html", context)

def create_item(request):
    if request.method == "POST":
        # Debug: Print request.POST data
        print(request.POST)
        
        item_form = ItemForm(request.POST)
        error_message = ""

        if item_form.is_valid():
            item = item_form.save(commit=False)
            item.owner = Character.objects.get(pk=request.POST['owner'])  # Mengambil owner berdasarkan ID yang diposting
            # Debug: Print item data
            print(item.name, item.amount, item.description, item.owner)
            
            item.save()
            return HttpResponseRedirect(reverse('main:show_main'))
        else:
            error_message = "Terdapat kesalahan dalam formulir, silakan periksa kembali."
    
    else:
        item_form = ItemForm()
        error_message = ""
    
    characters = Character.objects.all()  # Pindahkan deklarasi characters ke luar blok "else"
    context = {'item_form': item_form, 'characters': characters, 'error_message': error_message}
    return render(request, "item_list.html", context)



# Create your views here.
