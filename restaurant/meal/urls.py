from django.urls import path
from . import views

urlpatterns = [
    path('show_items/', views.showItems, name='showItems_page'),
]