from django.shortcuts import render
from django.views import generic #importiamo generic views
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy #per ridiregere dopo il logout e login

# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login') #così mandiamo subito al login dopo la registrazione