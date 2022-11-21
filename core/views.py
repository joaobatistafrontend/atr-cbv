from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView,View,ListView,UpdateView,DeleteView
from .models import Test,Produto
from .forms import TestForm
from braces.views import GroupRequiredMixin


class Home(TemplateView):
    def get(self,request):
        return render(request,'home.html')


class Autenticados(LoginRequiredMixin,CreateView):
    def get(self,request):
            form = TestForm()
            return render (request,'test.html',{'form':form}) 
    
    def post(self,request):
        form = TestForm(request.POST)
        if form.is_valid():
            print('foi valido')
            nome =form.data['nome']
            email =form.data['email']
            user = form.save()
            return redirect ('home')
        else:
            return redirect('home')


class Singup(View):
    def get(self,request):
            form = UserCreationForm()
            return render (request,'registration/singup.html',{'form':form}) 


    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        else:
            form = UserCreationForm()


class CriarProduto(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    template_name = 'crud/creat.html'
    model = Produto
    fields = '__all__'
    success_url = reverse_lazy ('home')
    group_required = u'administrador'

class ListaProduto(LoginRequiredMixin,ListView):
    template_name = 'crud/list.html'
    model = Produto
    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs)
        context ['produtos'] = Produto.objects.all()
        return context

class EditarProduto(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    template_name = 'crud/update.html'
    model = Produto
    fields = '__all__'
    success_url = reverse_lazy ('list')
    group_required = u'administrador'


class DeletarProduto(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    template_name = 'crud/delete.html'
    model = Produto
    success_url =  reverse_lazy('list')
    group_required = u'administrador'
