from django.shortcuts import render, get_object_or_404
from .models import Character, Item
from .forms import CharacterForm, ItemForm
from django.http import HttpResponseRedirect
import datetime, json
from main.forms import ProductForm
from main.models import Product
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import xml.etree.ElementTree as ET
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotFound

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
         login(request, user)
         response = HttpResponseRedirect(reverse("main:show_main")) 
         response.set_cookie('last_login', str(datetime.datetime.now()))
         return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def character_list(request):
    characters = Character.objects.all()
    return render(request, 'main/char_list.html', {'characters': characters})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'main/item_list.html', {'items': items})

@login_required(login_url='/login')

def show_main(request):
    products = Product.objects.all()
    user = request.user  # Info pengguna saat ini
    username = request.user.username
    
    # Filter karakter yang dimiliki oleh pengguna saat ini menggunakan relasi 'owner'
    characters = Character.objects.filter(user=request.user)  # Mengambil karakter berdasarkan pengguna saat ini
    
    # Filter item yang dimiliki oleh pengguna saat ini menggunakan relasi 'owner'
    items = Item.objects.filter(owner__user=user)
    
    jumlah_character = characters.count()  # Menghitung jumlah karakter
    jumlah_item = items.count()  # Menghitung jumlah item

    last_login = request.COOKIES.get('last_login', 'Belum ada informasi login terakhir')  # Mengambil 'last_login' dari cookie atau default jika tidak ada

    context = {
        'username': username,
        'class': 'PBP B',  # Kelas PBP kamu
        'app_name': 'Equinos',
        'products': products,
        'characters': characters,
        'items': items,
        'jumlah_character': jumlah_character,  # Sertakan jumlah karakter dalam konteks
        'jumlah_item': jumlah_item, 
        'last_login': last_login,
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
    if request.method == 'POST':
        character_form = CharacterForm(request.POST)
        if character_form.is_valid():
            character = character_form.save(commit=False)
            character.user = request.user  # Menyediakan pengguna yang terkait
            character.save()
            return redirect('main:show_main')
    else:
        character_form = CharacterForm()
    return render(request, "char_list.html", {'character_form': character_form})


def character_list(request):
    characters = Character.objects.filter(user=request.user)
    return render(request, 'char_list.html', {'characters': characters})

def create_item(request):
    error_message = ""
    
    if request.method == "POST":
        item_form = ItemForm(request.POST, user=request.user)

        if item_form.is_valid():
            item = item_form.save(commit=False)

            # Dapatkan karakter yang dipilih oleh pengguna melalui formulir
            selected_character = item_form.cleaned_data['owner']

            # Pastikan karakter tersebut dimiliki oleh pengguna saat ini
            if selected_character.user == request.user:
                item.owner = selected_character

                # Debug: Print item data
                print(item.name, item.amount, item.description, item.owner)

                item.save()
                return HttpResponseRedirect(reverse('main:show_main'))
            else:
                error_message = "Anda tidak memiliki izin untuk mengaitkan item dengan karakter ini."
        else:
            error_message = "Terdapat kesalahan dalam formulir, silakan periksa kembali."
    else:
        item_form = ItemForm()
    
    characters = Character.objects.filter(user=request.user)
    context = {'item_form': item_form, 'characters': characters, 'error_message': error_message}
    return render(request, "item_list.html", context)

def get_items(request):
    items = Item.objects.all()  # Gantilah sesuai dengan model Item Anda
    item_data = []

    for item in items:
        item_data.append({
            'name': item.name,
            'amount': item.amount,
            'description': item.description,
            'owner': item.owner.name if item.owner else None,  # Jika ada pemilik, gunakan nama pemilik, jika tidak, None
        })

    return JsonResponse({'items': item_data})

def add_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if item.amount > 0:
        item.amount += 1
        item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def reduce_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if item.amount > 0:
        item.amount -= 1
        item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def get_Item_json(request):
    product_item = Item.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

def get_Char_json(request):
    char_list = Character.objects.all()
    return HttpResponse(serializers.serialize('json', char_list))


@csrf_exempt  # mematikan proteksi CSRF; gunakan dengan hati-hati!
def create_item_ajax(request):    
    if request.method == "POST":
        item_form = ItemForm(request.POST, user=request.user)
        print(item_form.is_valid())
        if item_form.is_valid():
            item = item_form.save(commit=False)

            # Dapatkan karakter yang dipilih oleh pengguna melalui formulir
            selected_character = item_form.cleaned_data['owner']

            # Pastikan karakter tersebut dimiliki oleh pengguna saat ini
            if selected_character.user == request.user:
                item.owner = selected_character

                # Debug: Print item data
                print(item.name, item.amount, item.description, item.owner)

                item.save()
                return HttpResponse(b"CREATED", status=201)
    else:
        return HttpResponseNotFound() 
    
@csrf_exempt  # mematikan proteksi CSRF; gunakan dengan hati-hati!
def create_character_ajax(request):    
    if request.method == 'POST':
        character_form = CharacterForm(request.POST)
        if character_form.is_valid():
            character = character_form.save(commit=False)
            character.user = request.user  # Menyediakan pengguna yang terkait
            character.save()
            return HttpResponse(b"CREATED", status=201)

    else:
        return HttpResponseNotFound() 

@csrf_exempt 
def delete_item_ajax(request,id):
    if request.method == "POST":
        item = Item.objects.get(id=id)
        item.delete()
        return HttpResponse(b"OK", status=200)
    else:
        return HttpResponseNotFound()

# Create your views here.
