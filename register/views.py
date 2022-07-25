from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import RegisterForm
# Create your views here.
def register(request):
    form = RegisterForm()
    return render(request, 'register.html', {'form': form})
def submit(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        new_user = form.save()
        return HttpResponseRedirect('index.html')