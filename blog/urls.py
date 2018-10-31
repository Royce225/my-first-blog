"""Configuration des urls de notre blog"""

from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$',
     views.post_list, name='post_list'),
]