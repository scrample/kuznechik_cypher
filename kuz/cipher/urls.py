from django.urls import path

from .views import *


urlpatterns = [
    path('', cipher, name='home'),
    path('test', index, name='images'),
]