from django.urls import path,include
from .views import *
urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('singup/',Singup.as_view(),name='singup'),
    path('test/',Autenticados.as_view(),name='test'),
    path('creat/',CriarProduto.as_view(),name='creat'),
    path('list/',ListaProduto.as_view(),name='list'),
    path('update/<int:pk>/',EditarProduto.as_view(),name='update'),
    path('delete/<int:pk>/',DeletarProduto.as_view(),name='deleta'),

]
