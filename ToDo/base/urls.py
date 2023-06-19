from django.contrib import admin
from django.urls import path, include
from .views import index, remove

urlpatterns = [
    path('', index, name='index'),
    path('del/<str:pk>', remove),
]
