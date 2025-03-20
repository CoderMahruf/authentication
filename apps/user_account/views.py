from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic 
from django.contrib.auth import authenticate,login,logout 
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import LogoutRequiredMixin
from .forms import LoginForm,UserRegistrationForm
# Create your views here.

@method_decorator(never_cache, name='dispatch')
class Home(LoginRequiredMixin,generic.TemplateView):
    login_url = 'login'
    template_name = 'user_account/home.html'

@method_decorator(never_cache, name='dispatch')
class Login(LogoutRequiredMixin,generic.View):
    def get(self,*args,**kwargs):
        form = LoginForm
        return render(self.request,'user_account/login.html',{'form':form})

    def post(self,request,*args,**kwargs):
        form = LoginForm(self.request.POST)
        if form.is_valid():
            user = authenticate(self.request,
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password'))
            if user:
                login(self.request,user)
                return redirect('home')
            else:
                messages.warning(self.request, 'Wrong Credentials!')
                return redirect('login')
        return render(self.request,'user_account/login.html',{'form':form})

@method_decorator(never_cache, name='dispatch')
class Logout(generic.View):
    def get(self,*args,**kwargs):
        logout(self.request)
        return redirect('login')

@method_decorator(never_cache, name='dispatch')
class Registration(LogoutRequiredMixin,generic.CreateView):
    template_name = 'user_account/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self,form):
        messages.success(self.request,"Registration Successfull !")
        return super().form_valid(form) 