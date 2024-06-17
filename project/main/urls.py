from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "main"
urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('start', mentor_start, name='mentor_start'),
    path('list', mentor_list, name='mentor_list'),
    path('info', mentor_info, name='mentor_info'),
]