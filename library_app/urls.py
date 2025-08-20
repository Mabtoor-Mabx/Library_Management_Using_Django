# Import Libraries
from django.urls import path
from . import views

urlpatterns = [
    path('', views.author_list, name="author_list"),
    path('add-book/', views.add_book, name="add_book")
]
