from django.urls import path
from . import views

app_name = 'function'
urlpatterns = [
    path('get_entry/', views.get_entry, name='get_entry'),
]
