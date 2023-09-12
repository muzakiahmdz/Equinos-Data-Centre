from django.urls import path
from main.views import show_main
from . import views

app_name = 'main'

urlpatterns = [
    
    path('characters/', views.character_list, name='character_list'),
    path('items/', views.item_list, name='item_list'),
    path('', show_main, name='show_main'),

]
