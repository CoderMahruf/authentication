from django.shortcuts import render
from django.views import generic 
# Create your views here.

class Home (generic.TemplateView):
    template_name = 'user_account/home.html'