from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='main'),
    path('create_quote/', views.create_quote, name='create_quote'),
    path('create_author/', views.create_author, name='create_author'),
    path('details/<int:quote_id>/', views.details, name='details'),
    path('author_detail/<int:author_id>/', views.author_detail, name='author_detail'),
    path('delete/<int:quote_id>/', views.delete_quote, name='delete'),
    path('search_in_tags/<str:tag>/', views.search_in_tags, name='search_in_tags'),
    path('top_ten_tags/', views.top_ten_tags, name='top_ten_tags')
]