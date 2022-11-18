from django.urls import path,include
from .views import *
urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('singup/',Singup.as_view(),name='singup'),
    path('test/',Autenticados.as_view(),name='test')
]
