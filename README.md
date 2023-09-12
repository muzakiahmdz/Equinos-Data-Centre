# Equinos Data Centre 
![logo](https://th.bing.com/th/id/OIP.XuWVGpkbob-DpF8w345YGAHaEK?pid=ImgDet&rs=1)
# Muzaki Ahmad Ridho Azizy - 2206824924 - PBP B
# Link Aplikasi : [Link App](https://equinos.adaptable.app/main)
___________________________________________________________________________________________________________
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

class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField()
    category = models.CharField(max_length=50)
    description = models.TextField()
```
Terbuat model bernama Product berisi lima atribut, yaitu:
name = tipe data CharField dengan batasan 255 karakter.
amount = tipe data IntegerField.
price = tipe data IntegerField.
category = tipe data CharField dengan batasan 50 karakter.
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
