# Equinos Data Centre 
![logo](https://th.bing.com/th/id/OIP.XuWVGpkbob-DpF8w345YGAHaEK?pid=ImgDet&rs=1)
# Muzaki Ahmad Ridho Azizy - 2206824924 - PBP B
# Link Aplikasi : [Link App](https://equinos.adaptable.app/main)
___________________________________________________________________________________________________________
## Tugas 2
## Pengerjaan Aplikasi
* 1. Membuat proyek Django baru
Pertama, sebelum membuat proyek Django, persiapakn direktori lokal dan tidak lupa untuk mengaktifkan virtual environment dengan tujuan untuk mengisolasi package serta dependencies dari aplikasi saya agar tidak bertabrakan dengan versi satu sama lain yang ada di device yang saya guakan.
``` 
python -m venv env # inisiasi virtual environment
env\Scripts\activate.bat # untuk mengaktifkan virtual environment
```
Setelahnya lakukan instalasi beberapa modul. Pada direktori yang sama, saya membuat berkas requirements.txt berisi
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
Instalasi modul pada berkas tersebut dilakukan dengan menjalani perintah
```
pip install -r requirements.txt
```
Setelah modul diinstalasi, proyek Django bernama Equinos dapat dibuat
```
django-admin startproject Equinos .
```
Adapun ALLOWED HOST pada settings.py saya tambahkan "*" agar setiap hosts bisa mengakses aplikasi web
```
ALLOWED_HOSTS = ["*"]
```
Setelah itu saya menambahkan file .gitignore karena ada file-file yang tidak perlu git lacak.

* 2. Membuat aplikasi dengan nama main.
Pembuatan aplikasi dengan nama main pada proyek ini dilakukan dengan menjalankan perintah
```
python manage.py startapp main
```
Direktori main berisi struktur awal untuk aplikasi main yang sudah dibuatdan perlu didaftarkan pada proyek utama dengan cara membuka berkas settings.py di dalam proyek utama. Lalu tambahkan string nama aplikasi, main, pada variabel INSTALLED_APPS.
```
INSTALLED_APPS = [
    ...,
    main,
]
```
Setelah itu, Tambahkan direktori baru templates pada direktori main dan menambahkan file main.html yang berfungsi untuk mengatur tampilan aplikasi main pada web.

* 3. Melakukan routing pada proyek.
Untuk menghubungkan aplikasi main, edit berkas urls.py pada direktori utama dan impor fungsi include dari django.urls untuk mengimpor rute URL dari aplikasi main ke dalam berkas urls.py proyek.
```
from django.urls import path, include
```
Lalu, ditambahkan rute URL /main di dalam variabel urlpatterns.
```
urlpatterns = [
    ...
    path('main/', include('main.urls')),
]
```
* 4. Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.

name sebagai nama item dengan tipe CharField.
amount sebagai jumlah item dengan tipe IntegerField.
description sebagai deskripsi item dengan tipe TextField.

Membuat model pada aplikasi main dilakukan dengan mengisi kode berikut pada berkas models.py dalam direktori main.
```
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
```
Terbuat model bernama Product berisi lima atribut, yaitu:
name = tipe data CharField dengan batasan 255 karakter.
amount = tipe data IntegerField.
level = tipe data IntegerField.
description = tipe data TextField.
Setelah ini, diperlukan untuk mengubah struktur tabel basis data sesuai dengan perubahan model yang telah didefinisikan pada kode di atas dengan menjalankan perintah berikut.

* Membuat migrasi model
```
python manage.py makemigrations 
```
* Menerapkan migrasi ke dalam basis data lokal
```
python manage.py migrate 
```
* 5. Membuat sebuah fungsi pada views.py

    - ```
      def show_main(request):
            context = {
            'name': 'Muzaki Ahmad Ridho Azizy',
            'app_name': 'Equinos',
            'class': "PBP B"
            }
      ```
    - Pada file '`main.html`, saya dapat mengakses isi dari _context_ dengan contohnya menulis `{{name}}`. `{{name}}` akan mengambil isi `name` dari _context_ yaitu 'Muzaki Ahmad Ridho Azizy'

* 6. Membuat sebuah _routing_ pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`.
    - Impor `path` dari `django.urls` dan impor `show_main` dari `main.views`
    - Setelah itu, buat variable app_name yang berisi main seperti potongan kode berikut
    - ```app_name = 'main'```
    - Lalu menambahkan list bernama `urlpatterns` dan isi sebagai berikut
    -  ```
       urlpatterns = path('', show_main, name='show_main')

* 7. Melakukan _deployment_ ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    - Saya membuat repositori baru bernama Equinos Data Centre di github, lalu saya hubungkan direktori equinos di lokal ke repositori CarRel di Github. Setelah itu, saya lakukan _add, commit, push_. Kemudian saya lakukan deploy i adaptable (Tidak lupa untuk memilih _template_ deployment, tipe basis data, versi _python_, masukan command yang sesuai, nama aplikasi yang sesuai dan centang bagian HTTP Listener on PORT).

## Bagan Aplikasi Django
![logo](https://1.bp.blogspot.com/-u-n0WYPhc3o/X9nFtvNZB-I/AAAAAAAADrE/kD5gMaz4kNQIZyaUcaJJFVpDxdKrfoOwgCLcBGAsYHQ/s602/3.%2BPython%2BDjango%2B-%2BModul%2B2_Page2_Image5.jpg)
Ketika seorang user mengunjungi situs web Django melalui browser, permintaan mereka dikirimkan ke server sebagai HTTP Request. Server Django kemudian menggunakan sistem routing untuk mencocokkan pola URL dengan permintaan tersebut. Setelah pola URL ditemukan, Django memanggil fungsi yang terkait dalam berkas views.py, di mana logika aplikasi dan interaksi dengan basis data dilaksanakan sesuai dengan struktur yang telah didefinisikan dalam berkas models.py. Setelah semua operasi selesai, fungsi dalam views.py menghasilkan halaman web yang diminta oleh pengguna, umumnya dalam bentuk berkas HTML yang disebut "template." Berkas HTML ini disimpan dalam direktori "templates" untuk penggunaan berikutnya. Akhirnya, browser pengguna akan merender berkas HTML ini sebagai tanggapan (HTTP Response) dari server Django, memungkinkan mereka melihat tampilan yang dihasilkan.

## Penggunaan Virtual Environment
Virtual environment digunakan untuk memisahkan modul yang digunakan dalam proyek, mencegah konflik, dan menjaga keamanan. Ini memungkinkan pengembangan proyek yang lebih efisien dan terorganisir, menjauhkan kita dari masalah versi modul yang tidak cocok. Dengan virtual environment, proyek dapat dikembangkan secara paralel dengan proyek lain, lebih baik daripada menggunakan lingkungan global.

## MVC, MVT, MVM
- MVC (Model-View-Controller): Terdiri dari Model (data dan logika bisnis), View (tampilan), dan Controller (pengendali). Controller mengatur komunikasi antara Model dan View, memisahkan logika bisnis dari tampilan.

- MVT (Model-View-Template): Mirip dengan MVC, dengan Model yang mengelola data, View yang mengatur tampilan, dan Template yang mengontrol bagaimana data ditampilkan dalam HTML. Tidak ada Controller karena kerja ini sudah diatur oleh framework.

- MVVM (Model-View-ViewModel): Model mengurus data, View mengatur tampilan, dan ViewModel bertanggung jawab atas data binding, memungkinkan tampilan dan data berinteraksi tanpa perlu Controller.

Pentingnya pola desain adalah untuk membantu organisasi dan pengembangan yang lebih efisien dalam pengembangan perangkat lunak. Ketiganya menggunakan komponen yang berbeda. MVC menggunakan Controller untuk mengatur alur Model dan View. MVT menggunakan Template untuk mengatur tampilan HTML dan tidak perlu mengelola Controller karena sudah dilakukan oleh Framework. Sementara MVVM menggunakan ViewModel sebagai perantara untuk menghubungkan tampilan dengan data melalui pembaruan Model.


## Tugas 3
### Perbedaan antara form `POST` dan `GET` dalam Django
Dalam Django, POST dan GET adalah dua jenis metode HTTP yang berbeda yang digunakan untuk mengirim data dari browser ke server web. Mereka memiliki perbedaan utama dalam cara mereka mengirim dan memproses data:

Metode POST:
- Keamanan: Data dikirim secara rahasia karena tidak terlihat dalam URL.
- Pengiriman Data: Data dikirim dalam body permintaan HTTP, sehingga lebih aman untuk data yang sensitif atau besar.
- Batasan Ukuran: Tidak ada batasan ukuran teoretis untuk data yang dapat dikirim dengan metode POST, tetapi server dapat memiliki batasan praktis.
- Pemrosesan: Biasanya digunakan untuk mengirim data yang akan diproses oleh server, seperti saat mengirim formulir.
Pengaruh Terhadap Data: Memiliki pengaruh pada data server, seperti mengirim permintaan untuk membuat, memperbarui, atau menghapus data.

Metode GET:
- Keamanan: Data dikirim sebagai bagian dari URL, sehingga tidak aman untuk data sensitif atau rahasia.
- Pengiriman Data: Data dikirim sebagai parameter query string dalam URL.
- Batasan Ukuran: Terdapat batasan praktis pada panjang URL, yang berarti data yang dapat dikirim melalui metode GET terbatas.
- Pemrosesan: Biasanya digunakan untuk mengambil data dari server, seperti saat melakukan pencarian atau mengakses halaman web.
- Pengaruh Terhadap Data: Tidak seharusnya memiliki pengaruh pada data server. Secara tradisional, metode GET digunakan untuk membaca data tanpa mempengaruhi atau mengubahnya.


Metode POST digunakan untuk mengirim data ke server agar dapat diproses dan tidak bersifat idempoten, yang berarti setiap kali permintaan POST dipanggil, ia dapat menciptakan sumber daya baru atau mengubah yang sudah ada. Biasanya, permintaan POST digunakan untuk tujuan seperti membuat entitas baru atau memperbarui data yang ada, seperti saat mengirimkan formulir atau mengunggah file.

Sedangkan, metode GET digunakan untuk mengambil data dari server tanpa mengubahnya. Metode ini dianggap aman dan idempoten yang berarti dapat dipanggil berkali-kali tanpa mengubah hasilnya. Permintaan GET sering digunakan untuk mengambil data yang akan ditampilkan di halaman web, seperti daftar produk atau artikel.

### Perbedaan antara XML, JSON, dan HTML dalam pengiriman data

- XML (Extensible Markup Language):

XML memiliki struktur tag yang sangat deskriptif, sering digunakan untuk merepresentasikan data terstruktur.
Dalam XML, data dijelaskan dengan tag yang diletakkan dalam tanda <>. Ini membuat XML cocok untuk data yang memerlukan deskripsi yang sangat rinci.

```xml
<?xml version="1.0" encoding="utf-8"?>
<django-objects version="1.0">
    <object model="main.character" pk="3">
        <field name="name" type="CharField">leviathan</field>
        <field name="level" type="IntegerField">3000</field>
    </object>
    <object model="main.character" pk="4">
        <field name="name" type="CharField">gojo satoru</field>
        <field name="level" type="IntegerField">230</field>
    </object>
    <object model="main.character" pk="5">
        <field name="name" type="CharField">goku</field>
        <field name="level" type="IntegerField">90</field>
    </object>
</django-objects>

```

- JSON (JavaScript Object Notation):

JSON memiliki struktur mirip dengan dictionary Python, dengan pasangan key dan value yang disimpan dalam list.
Format JSON lebih ringkas dan mudah dibaca oleh manusia dibandingkan dengan XML, sehingga cocok digunakan untuk pertukaran data terstruktur antara server dan klien web. 

```json
"[{\"model\": \"main.item\", \"pk\": 1, \"fields\": {\"name\": \"Pistol revolver\", \"amount\": 1, \"description\": \"senjata api\", \"owner\": null}}]"

```

- HTML (Hypertext Markup Language):

HTML adalah bahasa markup yang digunakan untuk mengorganisir dan menampilkan data pada halaman web kepada pengguna akhir.
HTML digunakan untuk membuat elemen-elemen visual seperti teks, gambar, tautan, dan struktur halaman.

```html
<!-- Tampilan List Item -->
<h2>Item List</h2>
<ul>
    {% for item in items %}
        <li>{{ item.name }} - Amount: {{ item.amount }} - Description: {{ item.description }} - Owner: {{ item.owner.name }}</li>
    {% endfor %}
</ul>

<!-- Form Create Item -->
<h2 style="margin-top: 40px;">Create New Item</h2>
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ item_form.as_p }}
    <button type="submit" style="margin-top: 10px;">Create Item</button>
</form>

```
- Ringkasan: XML cocok untuk data yang memerlukan deskripsi yang sangat rinci. JSON lebih cocok untuk pertukaran data antara server dan klien web, sementara HTML digunakan untuk merender dan menampilkan konten pada halaman web.

### Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena memiliki format yang ringkas dan mudah dibaca sehingga developer tidak kesulitan memahami struktur data JSON ketimbang strukur data lainnya. Selain itu, JSON juga lebih efisien dalam hal ukuran penyimpanan data, memungkinkan transfer data yang lebih cepat dan efisien di seluruh jaringan. Ini menjadikannya pilihan yang sangat populer dalam pengembangan aplikasi web dan desain API RESTful yang berfokus pada kinerja dan kemudahan penggunaan.

### Implementasi Form dan Data Delivery pada Django
### 1. Membuat input `form` untuk menambahkan objek model pada app sebelumnya
Buat berkas `forms.py` pada direktori `main` yang akan mengimplementasikan library `django.forms`. Disini terdapat 2 form yang akan diimplementasikan yaitu character form dan item form. `(**NOTES: Untuk pengimplementasian item sama halnya dengan pengimplementasian character.)`

```python
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
```
Untuk merender tampilan form pada web, perlu dibuat sebuah view yang menghubungkan mekanisme form Django dengan template form. Dalam konteks ini, saya telah menambahkan beberapa impor modul dan fungsi berikut di dalam file views.py.

```python
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from .forms import CharacterForm, ItemForm


def create_character(request):
    character_form = CharacterForm(request.POST or None)

    if character_form.is_valid() and request.method == "POST":
        character_form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    characters = Character.objects.all()  # Menambahkan definisi characters
    context = {'character_form': character_form, 'characters': characters}  # Mengirim characters ke dalam konteks
    return render(request, "char_list.html", context)

```
Fungsi di atas digunakan untuk membuat karakter baru dalam aplikasi web dengan mengakses form karakter (CharacterForm) dan jika data yang dimasukkan valid dan metode permintaan adalah POST, maka karakter baru akan disimpan. Setelah itu, pengguna akan diarahkan kembali ke halaman utama aplikasi. Jika tidak valid atau metode permintaan bukan POST, maka akan menampilkan form karakter dengan daftar karakter yang sudah ada di dalam konteks.

mengedit fungsi `show_main` pada `views.py` dengan tambahan kode `    characters = Character.objects.all()` untuk mengambil data char yang ditambahkan dan `jumlah_character = len(characters)` untuk menghitung jumlah karakter yang telah dibuat.

Melakukan routing di `urls.py` pada direktori `main` dengan menambahkan kode berikut

```python
urlpatterns = [
    ...,
    path('create-character/', views.create_character, name='create_character'),
]
```
Setelah pola URL `view` ditambahkan pada `urls.py`, saya membuat `template` dengan nama `char_list.html`. Saya menggunakan `<form method="POST">` untuk mendefinisikan tipe form `POST` dan `{% csrf_token %}` untuk mencegah serangan CSFR (Cross-site request forgery), yaitu memaksa pengguna yang sudah terautentikasi untuk mengirim permintaan ke aplikasi web tanpa sepengetahuan mereka.
```html
    <!-- charlist.html -->
<h1>Character List</h1>
<table>
    <tr>
        <th>Name</th>
        <th>Level</th>
    </tr>
    {% for character in characters %}
        <tr>
            <td>{{ character.name }}</td>
            <td>{{ character.level }}</td>
        </tr>
    {% endfor %}
</table>

<h2>Add New Character</h2>
<form method="post">
    {% csrf_token %}
    {{ character_form.as_p }}
    <button type="submit">Submit Character</button>
</form>
```


### 2. Menambahkan 5 fungsi `views` untuk melihat pengiriman data 
Pada Tugas 2, kita sudah membuat satu fungsi `view` untuk melihat pengiriman data melalui format HTML. Berikut adalah 4 fungsi `views` yang ditambahkan untuk melihat pengiriman data melalui format:
`(**NOTE: Saat ini sedang coba dijelaskan hanya character. Untuk pengimplementasian item sama saja)`
- **JSON**, Membuat fungsi `show_json` pada `views.py` berisi kode di bawah untuk melihat dan mengembalikan tampilan data dalam format JSON.
    ```python
    def show_json(request):
    characters = Character.objects.all()
    items = Item.objects.all()
    # Menggabungkan daftar karakter dan daftar item
    data = list(characters) + list(items)

    # Mengonversi data menjadi JSON
    json_data = serializers.serialize("json", data)

    return JsonResponse(json_data, safe=False)
    ```
- **JSON berdasarkan Id**, Membuat fungsi `show_character_by_id` pada `views.py` berisi kode di bawah untuk melihat dan mengembalikan tampilan data dalam format JSON berdasarkan id yang diminta. `(**NOTE: Saat ini sedang coba dijelaskan hanya character. Untuk pengimplementasian item sama saja)`
    ```python
    def show_character_by_id(request, id):
    character = get_object_or_404(Character, pk=id)
    # Mengonversi objek karakter menjadi JSON
    json_data = serializers.serialize("json", [character])
    return JsonResponse(json_data, safe=False)
    ```
     Penggunaan get_object_or_404 memungkinkan kita untuk dengan mudah dan aman mengambil objek Character berdasarkan id yang diberikan tanpa harus menulis kode tambahan untuk penanganan kasus khusus jika objek tidak ditemukan.

- **XML**, Membuat fungsi `show_xml` pada `views.py` berisi kode di bawah untuk melihat dan mengembalikan tampilan data dalam format XML.
    ```python
    def show_xml(request):
    characters = Character.objects.all()
    items = Item.objects.all()

    # Menggabungkan daftar karakter dan daftar item
    data = list(characters) + list(items)

    # Mengonversi data menjadi XML
    xml_data = serializers.serialize("xml", data)

    return HttpResponse(xml_data, content_type="application/xml")
    ```
- **XML berdasarkan Id**, Membuat fungsi `show_character_by_id_xml` pada `views.py` berisi kode di bawah untuk melihat dan mengembalikan tampilan data dalam format XML berdasarkan id yang diminta.
    ```python
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
    ```
`ET.ElementTree` digunakan dalam fungsi `show_character_by_id_xml` untuk mengubah elemen XML karakter yang telah dibuat menjadi bentuk string dan kemudian menambahkannya ke respons HTTP. Ini memungkinkan pengiriman data karakter yang telah diambil dari database dalam format XML yang sesuai sebagai respons kepada pengguna yang mengaksesnya melalui permintaan web.

### 3. Membuat routing URL untuk masing-masing `views`
Setelah menambahkan 5 fungsi `views`, Tambahkan path kelima routing url tersebut pada `urls.py` dalam direktori `main`.

```python
[
    ...
    path('create-character/', views.create_character,    name='create_character'),
    path('create-item/', views.create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/character/<int:id>/', views.show_character_by_id_xml, name='show_character_by_id_xml'),
    path('xml/item/<int:id>/', views.show_item_by_id_xml, name='show_item_by_id_xml'),
    path('json/character/<int:id>/', views.show_character_by_id, name='show_character_by_id'),
    path('json/item/<int:id>/', views.show_item_by_id, name='show_item_by_id'),
]
```
Adapun fungsi path menerima 3 argumen: Pertama, pola path yang menentukan URL dengan bagian dinamis seperti <int:id> untuk menangkap nilai-nilai yang berbeda saat URL diakses; Kedua, pemanggilan fungsi view; Ketiga, nama unik untuk mengidentifikasi URL dalam aplikasi dan membuat tautan dari template.

### 4. Screenshot Postman
#### Hasil akses view HTML
![logo](https://i.imgur.com/md8OIWY.png)
#### Hasil akses view JSON
![logo](https://i.imgur.com/TiIhtcm.png)
#### Hasil akses view JSON berdasarkan id
- Character

![logo](https://i.imgur.com/uF0avXA.png)
- Item

![image](https://i.imgur.com/bjIg8Lt.png)
#### Hasil akses view XML
![Image](https://i.imgur.com/p53JInK.png)
#### Hasil akses view XML berdasarkan id
- Character

![image](https://i.imgur.com/JVDCb4B.png)
- Item

![Image](https://i.imgur.com/DYyV14B.png)

### Bonus Tugas 3. 
Untuk menampilkan jumlah data yang sudah tersimpan pada *database*, tambahkan potongan kode berikut pada show main
```python 
jumlah_character = len(characters)  # Menghitung jumlah karakter
jumlah_item = len(items)  # Menghitung jumlah item
```
Setelah itu tinggal adjust main.html agar dapat menampilkannya
```python
<p>Kamu memiliki {{ jumlah_character }} karakter pada aplikasi ini.</p> 
```
`(**NOTES: Lakukan hal yang serupa pada bagian html karakter)`