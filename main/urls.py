from django.urls import path
from . import views
from main.views import show_main,create_product, show_xml,show_json, show_character_by_id_xml, show_item_by_id_xml,show_character_by_id,show_item_by_id
app_name = 'main'

urlpatterns = [
    
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



]
