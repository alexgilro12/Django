from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        print(request.POST.get("username"))
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))

        print(user)
        if user is not None:
            login(request, user)
            return redirect('/plataformaRandom')

        return self.get(request)

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('login')