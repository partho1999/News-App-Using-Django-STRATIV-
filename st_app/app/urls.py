from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('newsfeed/', Newsfeed, name='newsfeed'),
    path('settings/', Settings, name='settings'),
    path('test/', test, name='test'),
    
]