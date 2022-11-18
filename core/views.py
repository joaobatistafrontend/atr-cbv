from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView,View
from .models import Test
from .forms import TestForm
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

    
    

# def singup(request):

#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect('home')
#     else:
#         form = UserCreationForm()
    
#     return render(request,'registration/singup.html',{
#         'form':form
#     })
