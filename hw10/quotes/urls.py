from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='root'),
    path("<int:page>", views.main, name="root_paginate"),
    path('author/<int:author_id>/', views.authors, name='author'),
    path('add_tag/', views.tag, name='add_tag'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
]