from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from .forms import LoginUserForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView

# Create your views here.

""" def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
    else:
        form = LoginUserForm()
    return render(request, 'users/login.html', {'form': form}) """

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': "Авторизация"}
    
   


""" def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login')) """

class LogoutUser(LogoutView):
    form_class = AuthenticationForm
    extra_context = {'title': 'Выход из системы'}
    template_name = 'users/login.html'