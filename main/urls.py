from django.urls import path
from . import views
from main.views import *
app_name = 'main'

urlpatterns = [

    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('characters/', views.character_list, name='character_list'),
    path('items/', views.item_list, name='item_list'),
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('create-character/', views.create_character, name='create_character'),
    path('create-item/', views.create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/character/<int:id>/', views.show_character_by_id_xml, name='show_character_by_id_xml'),
    path('xml/item/<int:id>/', views.show_item_by_id_xml, name='show_item_by_id_xml'),
    path('json/character/<int:id>/', views.show_character_by_id, name='show_character_by_id'),
    path('json/item/<int:id>/', views.show_item_by_id, name='show_item_by_id'),
    path('add_item/<int:item_id>/', views.add_item, name='add_item'),
    path('reduce_item/<int:item_id>/', views.reduce_item, name='reduce_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),



]
