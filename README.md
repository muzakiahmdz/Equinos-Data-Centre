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
<<<<<<< HEAD
`(**NOTES: Lakukan hal yang serupa pada bagian html karakter)`


### Tugas 4
## **No 1**
1. Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?

* UserCreationForm merupakan kelas formulir yang tersedia dalam Django, yang memudahkan proses penciptaan akun pengguna baru di aplikasi web. Kelas formulir ini secara bawaan menyertakan validasi untuk beberapa kolom seperti username, password1, dan password2.

* Keunggulan dari UserCreationForm meliputi:

- Integrasi yang Lancar: Formulir ini sudah menjadi bagian penting dari framework Django, sehingga mudah diintegrasikan ke dalam aplikasi web Django yang sedang dikembangkan.

- Validasi Otomatis: UserCreationForm menyediakan validasi otomatis yang mencakup pemeriksaan kata sandi agar memenuhi persyaratan tertentu, seperti panjang dan kompleksitas yang cukup. Selain itu, formulir ini juga memastikan bahwa username yang digunakan adalah unik.

- Dapat Disesuaikan: Kelas formulir ini bisa disesuaikan sesuai kebutuhan aplikasi. Ini memungkinkan penambahan kolom tambahan atau modifikasi pesan kesalahan yang ditampilkan.

- Keamanan Terjamin: Dibangun dengan memperhatikan prinsip-prinsip keamanan terbaik, termasuk penyimpanan yang aman untuk kata sandi pengguna.

* Kekurangan terkait UserCreationForm, yaitu:

- Fitur Terbatas: Jika diperlukan fitur tambahan seperti autentikasi dua faktor atau konfirmasi melalui email, pengembang perlu mengimplementasikannya secara terpisah, karena fitur-fitur tersebut tidak disediakan oleh UserCreationForm.

- Batasan dalam Validasi: Meskipun UserCreationForm menawarkan validasi bawaan, formulir ini mungkin memiliki keterbatasan dalam hal validasi data yang sangat spesifik sesuai kebutuhan aplikasi.

- Tampilan Standar: Tampilan formulir secara default mungkin kurang menarik dan perlu disesuaikan agar sesuai dengan estetika tampilan aplikasi yang dikembangkan.

## **No 2**
2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

* Autentikasi adalah proses verifikasi identitas pengguna, sementara otorisasi berkaitan dengan mengatur hak akses pengguna setelah mereka terautentikasi. Autentikasi dalam Django melibatkan penggunaan username dan password untuk memastikan identitas pengguna. Setelah autentikasi, langkah selanjutnya adalah otorisasi, yang menentukan apa yang dapat diakses atau dilakukan oleh pengguna yang telah terautentikasi.

* Keduanya sangat penting karena:

- Keamanan: Autentikasi dan otorisasi menjaga keamanan aplikasi. Tanpa autentikasi, siapa pun dapat mengakses data atau fungsionalitas yang seharusnya tidak mereka akses. Tanpa otorisasi, pengguna yang terautentikasi mungkin memiliki akses yang tidak terkontrol ke bagian-bagian sensitif dari aplikasi.

- Kontrol Akses: Otorisasi memungkinkan pengembang untuk mengontrol dengan tepat siapa yang dapat melakukan apa di dalam aplikasi. Ini membantu menjaga integritas data dan melindungi privasi pengguna.

- Kepatuhan: Dalam beberapa kasus, aplikasi perlu mematuhi peraturan dan regulasi tertentu yang mengharuskan implementasi autentikasi dan otorisasi yang kuat.

Dengan kombinasi autentikasi dan otorisasi yang baik, pengembang dapat memastikan bahwa pengguna hanya memiliki akses ke bagian dari aplikasi yang sesuai dengan peran dan hak akses mereka, sehingga menjaga keamanan dan keutuhan data.

## **No 3**
3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
* Cookies dalam konteks aplikasi web adalah file kecil yang disimpan di peramban web pengguna. Mereka digunakan untuk menyimpan informasi seperti data sesi pengguna atau preferensi untuk meningkatkan interaksi antara pengguna dan situs web.

* Dalam Django, cookies digunakan terutama untuk mengelola data sesi pengguna. Saat pengguna mengakses aplikasi web Django, cookie unik yang sering disebut sebagai sessionid diciptakan dan disimpan di peramban pengguna. Ketika pengguna kembali ke aplikasi, cookie ini dikirim kembali ke server Django, memungkinkan server mengenali dan mengembalikan data sesi yang terkait dengan pengguna tersebut. Ini sangat penting untuk menjaga kontinuitas sesi dan memungkinkan pengguna untuk tetap masuk dan menjaga preferensi mereka selama interaksi dengan aplikasi.

## **No 4**
4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
* Penggunaan cookies dalam pengembangan web tidak dapat dianggap aman secara default dan harus diperlakukan dengan serius dalam hal keamanan. Cookies berfungsi untuk menyimpan berbagai informasi, termasuk data sesi, preferensi, dan bahkan informasi login, yang secara alami membawa sejumlah risiko potensial yang harus diwaspadai.

* Beberapa risiko potensial yang perlu diwaspadai meliputi potensi serangan Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF), dan penggunaan cookies pihak ketiga yang dapat mengancam privasi pengguna.

* Untuk mengatasi risiko ini, tindakan keamanan harus diambil. Ini termasuk mengenkripsi data yang disimpan dalam cookies, menetapkan waktu kadaluarsa yang sesuai, serta memastikan bahwa cookies hanya digunakan dalam koneksi yang aman. Penerapan protokol keamanan yang ketat akan membantu melindungi data sensitif pengguna.


## **No 5**
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
   * A. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
     - Fungsi Registrasi
       - Import kode berikut di `views.py` pada dirketori aplikasi `main`
         ```py
         from django.shortcuts import redirect
         from django.contrib.auth.forms import UserCreationForm
         from django.contrib import messages  
         ```
       - Setelah itu, buat fungsi `register` yang berfungsi untuk meminta parameter request dan beiris
         ```py
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
         ```
       - Lalu buat file `register.html` pada direktori `templates` pada direktori aplikasi main dengan nama `bse.html`  dengan kode sebagai berikut
         ```py
            {% extends 'base.html' %}

            {% block meta %}
                <title>Register</title>
            {% endblock meta %}
            
            {% block content %}  
            
            <div class = "login">
                
                <h1>Register</h1>  
            
                    <form method="POST" >  
                        {% csrf_token %}  
                        <table>  
                            {{ form.as_table }}  
                            <tr>  
                                <td></td>
                                <td><input type="submit" name="submit" value="Daftar"/></td>  
                            </tr>  
                        </table>  
                    </form>
            
                {% if messages %}  
                    <ul>   
                        {% for message in messages %}  
                            <li>{{ message }}</li>  
                            {% endfor %}  
                    </ul>   
                {% endif %}
            
            </div>  
            
            {% endblock content %}
         ```
        - Setelah itu, import fungsi register yang sudah dibuat pada subdirektori `main` 
          ```py
          from main.views import register 
          ``` 
        - Setelah itu, tambahkan _path url_ ke dalam `urlpatterns` agar mengakses fungsi register yang sudah dibuat

          ```py
          path('register/', register, name='register'),
          ```
     
     - Fungsi Login
       - Import kode berikut di `views.py` pada direktori aplikasi main
       
         ```py
         from django.contrib.auth import authenticate, login        
         ```
       - Kemudian buat fungsi `login_user` di `views.py` pada direktori aplikasi main dengan kode berikut:
         ```py
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
         ```
       
        - Setelah itu, buat `login.html` pada direktori `main/templates` dengan kode berikut:
         ```py
         {% extends 'base.html' %}

         {% block meta %}
             <title>Login</title>
         {% endblock meta %}
            
         {% block content %}
            
         <div class = "login">
            
             <h1>Login</h1>
            
             <form method="POST" action="">
                 {% csrf_token %}
                 <table>
                     <tr>
                         <td>Username: </td>
                         <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                     </tr>
                                
                     <tr>
                         <td>Password: </td>
                         <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                     </tr>
            
                     <tr>
                         <td></td>
                         <td><input class="btn login_btn" type="submit" value="Login"></td>
                     </tr>
                 </table>
             </form>
            
             {% if messages %}
                 <ul>
                     {% for message in messages %}
                         <li>{{ message }}</li>
                     {% endfor %}
                 </ul>
             {% endif %}     
                    
             Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>
            
         </div>
            
         {% endblock content %}
            
         ```

        - Setelah itu, import pada urls.py pada subdirektori `main` dengan kode berikut:
         ```py
         from main.views import login_user
         ```
        - Setelah itu, tambahkan path url untuk login pada `urlpatterns` dengan kode sebagai berikut:
         ```py
         path('login/', login_user, name='login'),
         ```
     - Fungsi Logout
       - import kode berikut di `views.py` direktori aplikasi
         ```py
         from django.contrib.auth import logout
         ```
       - Buat fungsi `logout_user` di `views.py` direktori aplikasi dengan kode berikut:
         ```py
         def logout_user(request):
           logout(request)
           response = HttpResponseRedirect(reverse('main:login'))
           response.delete_cookie('last_login')
           return response
         ```
         Disini dilakukan penghapusan cookie dengan key `last_login` saat user logout

       - Setelah itu, tambahkan button logout di `main.html` dengan kode berikut
         ```py
         
            <a href="{% url 'main:logout' %}">
                <button>
                    Logout
                </button>
            </a>
            
         ```
       - Setelah itu, import fungsi `logout_user` di `urls.py` di subdirektori main
         ```py
         from main.views import logout_user
         ```
       - Setalah itu, routing ke dalam `urlpatterns` di `urls.py` di subdirektori main
         ```py
            path('logout/', logout_user, name='logout'),
         ```
     - Restriksi akses aplikasi
       - import `login_required` di `views.py`
       - Tambahkan `@login_required(login_url='/login')` di atas fungsi `show_main`
   


   * B. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
   ![image](https://i.imgur.com/umDHtbM.png) 
   ![image](https://i.imgur.com/GXs6Xij.png)
   

   * C.Menghubungkan model Item dengan User 
     - Melakukan import pada `models.py`
     ```py
     from django.contrib.auth.models import User
     ```
     - Sesuaikan pada  `models.py`
     ```py
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
     ```
     - Tambahkan potongan kode pada `create_item` di `views.py` agar item yang dibuat terasosiasi pada user
     ```py
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
     ```
     - Setelah itu, ubah fungsi `show_main` menjadi

     - ```py
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

       ```
       
     - Setelah itu, jangan lupa lakukan migrasi
   
    
   * D. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.  
     - Menampilkan username pengguna
       Pada fungsi `show_main` di `views.py` ubah isi context dengan key `name` menjadi berikut
       ```py
       'name': request.user.username,
       ```
     - Menerapkan cookies last login
       Penerapannya sudah dijelaskan diatas untuk menampilkan last login, lalu tambahkan kode berikut pada context di `show_main`
       ```py
       'last_login': request.COOKIES['last_login'],
       ```
     - Tambahkan kode berikut di `main.html`
       ```py
       <h5>Last login session: {{ last_login }}</h5>
       ```
     - Tampilan 
       ![image](https://i.imgur.com/tVMi9Bz.png)

## **No 6**
6. Bonus
   - Buat tiga tombol yaitu + Amount (untuk increment amount) , - Amount (untuk decrement amount), dan Delete (delete item)
   ```html
    <tr>
        <td>{{ item.name }}</td>
        <td>{{ item.amount }}</td>
        <td>{{ item.description }}</td>
        <td>
            <form method="post" action="{% url 'main:add_item' item.id %}">
                {% csrf_token %}
                <button type="submit">Tambah</button>
            </form>
            <form method="post" action="{% url 'main:reduce_item' item.id %}">
                {% csrf_token %}
                <button type="submit">Kurang</button>
            </form>
            <form method="post" action="{% url 'main:delete_item' item.id %}">
                {% csrf_token %}
                <button type="submit">Hapus</button>
            </form>
        </td>
    </tr>
   ```
    - Tambahkan URL dan View untuk Menangani Aksi Tambah, Kurang, dan Hapus:

    Di dalam urls.py, tambahkan URL dan view yang akan menangani aksi tambah, kurang, dan hapus item.

    ```py
    Copy code
    path('add_item/<int:item_id>/', views.add_item, name='add_item'),
    path('reduce_item/<int:item_id>/', views.reduce_item, name='reduce_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    ```

    - Kemudian, di dalam views.py, buat tiga view untuk menangani aksi-aksi tersebut:

    ```python
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

    ```

    - Mengatasi Masalah Tidak Ada Owner saat Menambahkan Item:

    Untuk mengatasi masalah bahwa item yang ditambahkan tidak memiliki owner, perbarui logic di views.py saat membuat objek item baru. Daripada menggunakan pemilihan karakter di dalam form, tentukan pemiliknya berdasarkan pengguna yang saat ini masuk. Misalnya:

    ```python
    def create_item(request):
        error_message = ""

        if request.method == "POST":
            item_form = ItemForm(request.POST)

            if item_form.is_valid():
                item = item_form.save(commit=False)

                # Dapatkan karakter yang dimiliki oleh pengguna saat ini
                user_characters = Character.objects.filter(user=request.user)

                # Pastikan pengguna memiliki karakter
                if user_characters.exists():
                    # Pilih karakter pertama pengguna sebagai pemilik item
                    selected_character = user_characters.first()

                    item.owner = selected_character

                    # Debug: Print item data
                    print(item.name, item.amount, item.description, item.owner)

                    item.save()
                    return HttpResponseRedirect(reverse('main:show_main'))
                else:
                    error_message = "Anda tidak memiliki karakter untuk mengaitkan item ini."
            else:
                error_message = "Terdapat kesalahan dalam formulir, silakan periksa kembali."
        else:
            item_form = ItemForm()

        characters = Character.objects.filter(user=request.user)
        context = {'item_form': item_form, 'characters': characters, 'error_message': error_message}
        return render(request, "item_list.html", context)

    ```


### Tugas 5
# 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

Element selector dalam CSS digunakan untuk memilih elemen HTML berdasarkan nama elemen atau tag-nya. Ada beberapa manfaat yang dapat diberikan oleh penggunaan element selector, dan waktu yang tepat untuk menggunakannya tergantung pada kebutuhan desain dan struktur halaman web:

- Seleksi Spesifik Elemen: Element selector memungkinkan untuk memilih elemen HTML dengan sangat spesifik berdasarkan nama elemen. Misalnya, dapat menggunakan p untuk memilih semua elemen paragraf dalam dokumen.

Kapan menggunakannya: Ketika ingin menerapkan gaya atau aturan tertentu ke semua elemen dengan tag yang sama di seluruh situs web. Misalnya, jika ingin memastikan bahwa semua paragraf dalam situs memiliki font yang sama.

- Seleksi Elemen Tertentu: juga dapat menggunakan element selector bersama dengan selektor lain, seperti class atau ID, untuk memilih elemen yang lebih spesifik. Contohnya adalah div.sidebar p, yang memilih semua elemen paragraf yang berada di dalam elemen div dengan class "sidebar".

Kapan menggunakannya: Ketika perlu memilih elemen-elemen spesifik di dalam elemen lain untuk mengatur gaya atau perilaku mereka.

- Mengatur Nilai Default: Element selector juga dapat digunakan untuk mengatur nilai default untuk elemen-elemen tertentu. Misalnya, dapat menggunakan ul untuk mengatur nilai default untuk daftar tak terurut (unordered list) dalam situs.

Kapan menggunakannya: Ketika ingin mengatur nilai default untuk semua elemen dengan tag tertentu dalam dokumen, dan kemudian menyesuaikannya lebih lanjut dengan selektor lain jika diperlukan.

- Meningkatkan Kejelasan Kode: Element selector dapat digunakan untuk meningkatkan kejelasan kode CSS. Saat membaca kode CSS, pengguna atau pengembang lain dapat dengan mudah memahami bahwa sedang mengatur gaya untuk elemen dengan tag tertentu.

Kapan menggunakannya: Selalu gunakan element selector ketika ingin mengatur gaya atau perilaku elemen berdasarkan tag HTML-nya untuk meningkatkan kejelasan kode.

Namun, perlu diingat bahwa penggunaan element selector dengan sangat spesifik (misalnya, body p untuk memilih semua elemen paragraf dalam halaman web) dapat mengakibatkan seleksi yang sangat luas dan mempengaruhi kinerja halaman web. Oleh karena itu, selalu pertimbangkan penggunaan selektor yang lebih spesifik seperti class atau ID jika memungkinkan.


# 2. Jelaskan HTML5 Tag yang kamu ketahui.
* | No | Tag           |Penjelasan |
   |----|---------------|---|
   | 1  | `<html>`      |  digunakan untuk mengawali dan mengakhiri seluruh kode atau dokumen HTML
   | 2  | `<head>`      |  digunakan untuk menyertakan informasi meta, judul halaman web, dan menghubungkan html dengan _stylesheet_ serta Javascript
   | 3  | `<title>`     |  digunakan untuk menentukan judul halaman web yang ditampilkan
   | 4  | `<meta>`      |  digunakan untuk mendefinisikan metadata tentang halaman web, seperti karakter set, deskripsi, dan informasi lain yang relevan.
   | 5  | `<link>`      |  digunakan untuk mengawali dan mengakhiri seluruh kode atau dokumen HTML
    | 6  | `<body>`      |   berisi konten utama halaman web yang akan ditampilkan kepada pengguna, seperti teks, gambar, dan elemen-elemen lainnya.
   | 7  | `<h1> - <h6>` |  Tag-tag ini digunakan untuk mengatur tingkat judul atau heading. h1 adalah yang tertinggi , sementara h6 adalah yang terendah.HTML
   | 8  | `<p>`         |  digunakan untuk membuat paragraf teks.
   | 9  | `<a>`         |  digunakan untuk membuat tautan atau hyperlink ke halaman web atau sumber daya lainnya.
   | 10 | `<img>`      |  digunakan untuk menampilkan gambar di halaman web.
   | 11 | `<ul>`      |  digunakan untuk membuat daftar tak terurut (unordered list), yang berisi elemen-elemen dalam bentuk daftar bulleted.
   | 12 | `<ol>`      |  digunakan untuk membuat daftar terurut (ordered list), yang berisi elemen-elemen dalam bentuk daftar bernomor.
   | 13 | `<li>`      |  digunakan untuk mendefinisikan elemen-elemen dalam daftar (baik daftar tak terurut maupun terurut).
   | 14 | `<div>`      |  elemen blok yang digunakan untuk mengelompokkan dan mengatur elemen-elemen HTML lainnya dalam sebuah kotak atau wadah. Ini sering digunakan dalam desain tata letak halaman.
   | 15 | `<span>`      |  digunakan untuk mengaplikasikan gaya atau mengelompokkan sebagian kecil dari teks atau elemen dalam dokumen.


# 3. Jelaskan perbedaan antara margin dan padding.
* | Perbedaan | Margin   | Padding                                                       |
   |-----------|----------|---------------------------------------------------------------|
   | Fungsi Utama         | Ruang di luar elemen, mempengaruhi tata letak elemen dalam hubungannya dengan elemen lain di sekitarnya. | Ruang di dalam elemen, mempengaruhi tampilan dan tata letak konten elemen.
   | Dampak pada Ukuran       | Margin dapat memengaruhi ukuran keseluruhan elemen, membuatnya terlihat lebih besar dan memiliki ruang kosong di sekitarnya. | Padding tidak memengaruhi ukuran keseluruhan elemen; ukuran elemen tetap sama, hanya kontennya yang terdorong ke dalam.
   | Pengaruh terhadap Konten         | Tidak ada pengaruh langsung terhadap konten elemen. | Memengaruhi tampilan dan tata letak konten dalam elemen.
   | Tampilan Visual       | Tampilan visual dari margin adalah ruang kosong di sekitar elemen yang ditentukan oleh warna latar belakang elemen lain di sekitarnya | Tampilan visual dari padding adalah ruang kosong di sekitar konten elemen, yang ditentukan oleh warna latar belakang elemen itu sendiri.
   | Pengaruh terhadap Konten         | Margin dapat digunakan dengan elemen blok maupun inline. | Padding biasanya digunakan dengan elemen blok; elemen inline memiliki padding horizontal tetapi tidak memiliki padding vertikal.

# 4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
* Bootstrap:

- Komponen Lebih Kaya: Bootstrap menyediakan beragam komponen UI yang sudah dirancang dengan baik, seperti navbar, tombol, kartu, formulir, dll. Ini membuatnya sangat cocok untuk proyek-proyek yang memerlukan komponen-komponen UI yang kaya dan kompleks.

- Desain Responsif Terintegrasi: Bootstrap telah dirancang untuk responsif secara bawaan, yang berarti komponen-komponennya akan menyesuaikan diri dengan baik dengan perangkat seluler dan desktop.

- Lebih Mudah untuk Pemula: Bootstrap memiliki dokumentasi yang sangat baik dan banyak tutorial yang tersedia, sehingga cocok untuk pemula yang ingin memulai dengan cepat.

- Tema Bawaan: Bootstrap memiliki tema bawaan yang dapat gunakan sebagai dasar untuk mengatur gaya situs web.

- Kekuatan CSS dan JavaScript: Bootstrap memiliki banyak opsi pengaturan CSS dan JavaScript yang dapat diaktifkan atau dinonaktifkan sesuai kebutuhan, yang memberikan fleksibilitas tambahan dalam pengembangan.

Kapan Menggunakan Bootstrap:

Saat memerlukan komponen-komponen UI yang sudah dirancang dengan baik.
Ketika ingin memulai dengan cepat dan memiliki dokumentasi yang kuat sebagai panduan.
Untuk proyek-proyek yang memerlukan desain responsif yang sudah terintegrasi secara otomatis.
Jika ingin menggunakan tema bawaan sebagai dasar desain situs.

* Tailwind CSS:

- Pendekatan Utility-First: Tailwind CSS mengadopsi pendekatan "utility-first," yang berarti membangun tampilan situs dengan menggabungkan kelas-kelas utilitas CSS ke dalam elemen HTML. Ini memberikan tingkat fleksibilitas yang tinggi dalam mendesain tampilan.

- Custom Styling: Tailwind memungkinkan dengan mudah menyesuaikan tampilan situs dengan mendefinisikan gaya sendiri menggunakan konfigurasi yang fleksibel.

- Kontrol yang Lebih Besar: memiliki kontrol yang lebih besar atas setiap aspek desain, tetapi ini juga bisa menjadi kurva belajar yang lebih tinggi.

- Ringan: Tailwind CSS lebih ringan dalam hal ukuran file dibandingkan dengan Bootstrap karena hanya menghasilkan CSS yang diperlukan.

Kapan Menggunakan Tailwind CSS:

Saat ingin memiliki kontrol yang tinggi atas desain tampilan.
Untuk proyek-proyek yang memerlukan desain unik dan tidak ingin terlalu bergantung pada komponen-komponen UI yang sudah ada.
Jika memiliki pengalaman dengan pendekatan utility-first atau ingin mempelajarinya. Untuk menghindari overhead dari komponen yang tidak digunakan.

## **No 5**
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
* Kustomisasi desain pada templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:
- Kustomisasi halaman login, register, dan tambah inventori

* Halaman Login
Pada halaman login saya mengimplementasi CSS itu sendiri kepada `login.html`. Berikut implementasinya:

```
/* CSS untuk halaman login */
.login {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f4f4f4;
    border-radius: 5px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    text-align: center;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.login h1 {
    text-align: center;
    font-size: 20px;
    margin-bottom: 20px;
    color: #333;
}

.login table {
    width: 100%;
}

.login .form-control {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-bottom: 10px;
    text-align: center;
}

.login .login_btn {
    background-color: #007bff;
    color: #fff;
    text-align: center;
    border: none;
    border-radius: 10px;
    padding: 6px 20px;
    cursor: pointer;
}

.login .login_btn:hover {
    background-color: #0056b3;
}

.login .message {
    margin-top: 7px;
    color: red;
}

.login a {
    font-size: 14px;
    text-decoration: none;
    color: #007bff;
}

.login a:hover {
    text-decoration: underline;
}

```
Di dalam kode CSS tersebut, Saya telah mendefinisikan gaya-gaya untuk halaman login. Berikut adalah penjelasan singkat untuk beberapa gaya yang telah saya tentukan:

.login: Ini adalah kelas untuk elemen utama yang mengelilingi halaman login. Saya telah mengatur beberapa properti seperti lebar maksimum, margin tengah, latar belakang, dan bayangan.

.login h1: Ini adalah gaya untuk judul "Login" di dalam halaman. Saya telah mengatur ukuran font dan warna teks.

.login table: Gaya ini tampaknya digunakan untuk mengatur lebar tabel.

.login .form-control: Gaya ini digunakan untuk mengatur elemen input dengan kelas .form-control. Saya telah mengatur lebar, padding, border, dan border-radius.

.login .login_btn: Ini adalah gaya untuk tombol "Login". Saya telah mengatur latar belakang tombol, warna teks, dan beberapa properti lainnya.

.login .message: Gaya ini tampaknya digunakan untuk pesan kesalahan atau pesan lain yang ingin ditampilkan di halaman login. Saya telah mengatur margin atas dan warna teks merah.

.login a dan .login a:hover: Ini adalah gaya untuk tautan di halaman login dan tautan saat dikursori. Saya telah mengatur ukuran font, dekorasi teks, dan warna tautan.


* Halaman Register 
Saya juga meinimplementasikan CSS ke dalam `register.html`. Berikut perubahannya:
```
<style>
/* CSS untuk halaman pendaftaran */
.register {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f4f4f4;
    border-radius: 5px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    text-align: center;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-family: Arial, sans-serif;
}

.register h1 {
    font-size: 24px;
    margin-bottom: 20px;
    color: #333;
}

.register table {
    width: 100%;
}
.register table label {
    display: block;
    text-align: left;
    margin-bottom: 5px;
    color: #333;
}


.register .form-control {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-bottom: 10px;
}

.register .submit-btn {
    background-color: #28a745;
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    cursor: pointer;
}

.register .submit-btn:hover {
    background-color: #1e7e34;
}

.register .message {
    margin-top: 10px;
    color: red;
}

.register a {
    text-decoration: none;
    color: #007bff;
}

.register a:hover {
    text-decoration: underline;
}
</style>
```

* Saya juga melakukan beberap perubahan di `main.html`. Salah satu contohnya adalah penambahana warna pada tombol tambah-kurang-hapus pada tabel item. 
```
<form method="post" action="{% url 'main:add_item' item.id %}">
    {% csrf_token %}
    <button type="submit" class="btn btn-success">Tambah</button>
</form>
<form method="post" action="{% url 'main:reduce_item' item.id %}">
    {% csrf_token %}
    <button type="submit" class="btn btn-warning">Kurang</button>
</form>
<form method="post" action="{% url 'main:delete_item' item.id %}">
    {% csrf_token %}
    <button type="submit" class="btn btn-danger">Hapus</button>
</form>

```

Tombol "Tambah" memiliki kelas btn-success, yang memberikan warna hijau.
Tombol "Kurang" memiliki kelas btn-warning, yang memberikan warna kuning.
Tombol "Hapus" memiliki kelas btn-danger, yang memberikan warna merah.

Jadi, implementasi penambahan warna pada tombol-tombol tersebut telah dilakukan dengan menggunakan kelas-kelas Bootstrap yang sesuai, seperti yang terlihat dalam kode di atas. Kita juga dapat menyesuaikan kelas-kelas ini sesuai dengan preferensi warna atau tampilan yang Anda inginkan dengan mengacu pada dokumentasi Bootstrap untuk lebih banyak pilihan warna dan gaya tombol.

## Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card.
Saya telah mengimplementasikan kartu Bootstrap (Bootstrap card) di beberapa bagian dalam template HTML Anda. Kartu Bootstrap adalah komponen UI yang digunakan untuk menampilkan konten dalam kotak dengan latar belakang dan bingkai yang konsisten. Berikut ini adalah detail penggunaan kartu pada template Anda:

- Kartu untuk Menampilkan Username dan Class: 
```html
<div class="card">
    <div class="card-header">
        <h5 class="card-title" style="color: #666;">Username:</h5>
    </div>
    <div class="card-body">
        <p class="card-text">{{ username }}</p>
    </div>
</div>
```

Penggunaan: Kartu ini digunakan untuk menampilkan informasi "Username" dalam sebuah kotak dengan latar belakang dan bingkai yang konsisten.


- Kartu untuk Menampilkan Character List:

``` html
<div class="card">
    <div class="card-header">
        <h2 class="card-title" style="color: #666;">Character List</h2>
    </div>
    <div class="card-body">
        <!-- Isi konten karakter di sini -->
    </div>
</div>
```
Penggunaan: Kartu ini digunakan untuk menampilkan daftar karakter dalam kotak yang memiliki judul "Character List" dengan latar belakang dan bingkai yang konsisten.

- Kartu untuk Membuat Item Baru:

```html
<div class="card">
    <div class="card-header">
        <h2 class="card-title" style="color: #666;">Create New Item</h2>
    </div>
    <div class="card-body">
        <!-- Form untuk membuat item baru di sini -->
    </div>
</div>
```
Penggunaan: Kartu ini digunakan untuk menampilkan formulir untuk membuat item baru dalam kotak dengan judul "Create New Item" dengan latar belakang dan bingkai yang konsisten.

- Kartu untuk Menampilkan Item List:

```html
<div class="card">
    <div class="card-header">
        <h2 class="card-title" style="color: #666;">Item List</h2>
    </div>
    <div class="card-body">
        <!-- Tabel untuk menampilkan daftar item di sini -->
    </div>
</div>
```
Penggunaan: Kartu ini digunakan untuk menampilkan daftar item dalam sebuah kotak dengan judul "Item List" dengan latar belakang dan bingkai yang konsisten.

= Kartu untuk Menampilkan Sesi Terakhir Login:

```html
<div class="card">
    <div class="card-body">
        <h5 class="text-center" style="color: #666; margin-top: 20px;">Sesi terakhir login: {{ last_login }}</h5>
    </div>
</div>
```
Penggunaan: Kartu ini digunakan untuk menampilkan informasi tentang sesi terakhir login dalam sebuah kotak dengan teks berwarna dan bingkai yang konsisten.

Kartu Bootstrap digunakan di berbagai bagian dari halaman Anda untuk mengatur dan memformat konten dalam bentuk yang rapi dan konsisten. Mereka memungkinkan Anda untuk menampilkan informasi dengan gaya yang menarik dan sesuai dengan desain umum situs web Anda.

# Tugas 6
## **No 1**
1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
* Asynchronous programming memungkinkan eksekusi tugas-tugas secara paralel atau sekuensial tanpa harus menunggu tugas sebelumnya selesai, sehingga dapat meningkatkan responsivitas dan efisiensi program, terutama dalam kasus operasi I/O yang memerlukan waktu lama atau komunikasi dengan sumber eksternal. Di sisi lain, synchronous programming mengeksekusi tugas-tugas secara berurutan, yang sederhana namun dapat menyebabkan program terblokir jika terdapat tugas dengan waktu eksekusi yang lama. Pemilihan antara keduanya harus didasarkan pada kebutuhan aplikasi dan kompleksitas tugas yang dihadapi.


## **No 2**
2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini. 
* Paradigma event-driven programming merupakan di mana alur eksekusi program ditentukan oleh sejumlah peristiwa, seperti tindakan _user_ (klik mouse, klik keyboard) atau pesan dari program lain atau thread. Contohnya, pada tugas ini, event-driven programming digunakan untuk menangani event yang terjadi pada aplikasi web seperti klik tombol, input teks, dan lain-lain.
* Contoh penerapannya pada tugas kali ini adalah: 
   ` document.getElementById("button_add_char").onclick = addChar `


## **No 3**
3. Jelaskan penerapan asynchronous programming pada AJAX.
* Dalam AJAX, asynchronous programming memungkinkan kita untuk mengambil informasi dari server tanpa perlu memperbarui seluruh halaman. Dengan _asynchronous programming_, saat permintaan dikirim ke server, eksekusi program lain dapat berlanjut tanpa menunggu balasan dari server. Begitu balasan diterima, program kemudian menjalankan fungsi tertentu untuk memproses informasi tersebut. Pendekatan ini meningkatkan efisiensi dan responsivitas aplikasi web, memberikan pengalaman yang lebih mulus bagi pengguna tanpa perlu menunggu pembaruan halaman penuh.


## **No 4**
4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan
* Sejak munculnya AJAX, library jQuery telah menjadi instrumen utama dalam implementasinya, menawarkan cara sederhana untuk melakukan permintaan asinkron. Keunggulan dari AJAX melalui jQuery terletak pada kompatibilitas lintas browser-nya, memastikan fungsionalitas bahkan pada browser yang lebih tua yang belum mendukung teknologi web terkini. Namun, seiring berjalannya waktu, browser modern telah menawarkan Fetch API yang merupakan fitur bawaan browser modern, memungkinkan permintaan asinkron tanpa kebutuhan library tambahan. Fetch API menyediakan fleksibilitas lebih dalam mengelola permintaan dan respons, dan mendukung teknologi terbaru seperti promises dan async/await. Mengingat Fetch API adalah standar web modern, dukungan lintas browser sudah luas, dan ini menghilangkan kebutuhan library tambahan. 
* Untuk sekarang, Fetch API sering kali dipilih karena kode yang lebih efisien, tidak adanya ketergantungan, dan kapabilitas aslinya. Meskipun demikian, untuk aplikasi yang fokus pada kompatibilitas atau telah mengadopsi jQuery sepenuhnya, AJAX melalui jQuery masih memiliki tempatnya.

## **No 5**
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
* Mengubah tugas 5 yang dibuat sebelumnya menjadi menggunakan AJAX
  - AJAX GET
    * Membuat Fungsi untuk Mengembalikan Data JSON
    ```py
    def get_Item_json(request):
    product_item = Item.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

    def get_Char_json(request):
    char_list = Character.objects.all()
    return HttpResponse(serializers.serialize('json', char_list))

    ```
    * Membuat fungsi create ajax
    ```py 
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
    
    ```
    * Setting url
    ```
    path('get-item-json/', get_Item_json, name='get_item_json'),
    path('get-char-json/', get_Char_json, name='get_char_json'), 

    ```
    * Ubah bagian table
    ```
    <table id="product_table"></table>
    ```
    * Taro bagian getter ke dalam script
    ```py 
    <script>
    async function getItem() {
        return fetch("{% url 'main:get_item_json' %}").then((res) => res.json())
    }
    async function getChar() {
        return fetch("{% url 'main:get_char_json' %}").then((res) => res.json())
    }
    <script/>

    ```
    - AJAX POST
    ```
    * Tambahkan add product AJAX (AJAX POST)
    ```
    function addItem() {
        fetch("{% url 'main:create_item_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(refreshItems)

        document.getElementById("form").reset()
        return false
    }
    document.getElementById("button_add").onclick = addItem

    ```

    * Atur routing 
    ```
    path('create-item-ajax/', views.create_item_ajax, name='create_item_ajax'),
    path('create-character-ajax/', views.create_character_ajax, name='create_character_ajax'),
    ```

    * Buatlah function async dalam tabel (cth disini tabel item)
    ```
    async function refreshItems() {
        document.getElementById("product_table").innerHTML = ""
        const products = await getItem()
        let htmlString = `<tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Description</th>
            <th>Owner</th>
            <th> Delete </th>
        </tr>`
        products.forEach((item) => {
            htmlString += `\n<tr>
            <td>${item.fields.name}</td>
            <td>${item.fields.amount}</td>
            <td>${item.fields.description}</td>
            <td>${item.fields.owner}</td>
            <td><button type="button" class="btn btn-danger" onclick="deleteItemAJAX(${item.pk})">Delete</button></td>
        </tr>` 
        })
        
        document.getElementById("product_table").innerHTML = htmlString
    }

    refreshItems()
    ```

- Melakukan perintah collectstatic
    - Pada settings.py, tambahkan `STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')` di bawah STATIC_URL.
    - Jalankan perintah python manage.py collectstatic untuk mengumpulkan semua file static ke folder staticfiles.

## **No 6**
* BONUS tugas 6
  - Menambahkan fungsionalitas hapus dengan menggunakan AJAX DELETE
 ```python
        @csrf_exempt 
    def delete_item_ajax(request,id):
        if request.method == "POST":
            item = Item.objects.get(id=id)
            item.delete()
            return HttpResponse(b"OK", status=200)
        else:
            return HttpResponseNotFound()
      ```
    - Lakukan routing pada `urls.py`
      ```python
        path('delete-item-ajax/<int:id>/', delete_item_ajax, name='delete_item_ajax'),
      ```
    - Buat function delete di main
    ```
    function deleteItemAJAX(id){
        fetch(`/delete-item-ajax/${id}`, {
            method: "POST",
        
        }).then(refreshItems)

        document.getElementById("form").reset()
        return false
    }
    ```
=======
`(**NOTES: Lakukan hal yang serupa pada bagian html item)`
>>>>>>> 1bf2a98a90105d703f4b810111b2b344451396e4
