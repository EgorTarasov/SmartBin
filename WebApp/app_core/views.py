from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import BaseCreateView

from .forms import *
from .models import *


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def index(request):
    context = dict()
    bins = Bin.objects.all()
    context['bins'] = bins
    return render(request, 'index.html', context)


def create_bin(request):
    context = dict()
    form = CreateBinForm()
    context['form'] = form
    if request.method == 'POST':
        form = CreateBinForm(request.POST)
        if form.is_valid():
            new_bin = Bin(
                name=form.cleaned_data['name'],
                ip_address=form.cleaned_data['ip_address']
            )
            new_bin.check_ip()
            new_bin.save()
            return redirect('index')
        else:
            return render(request, 'create_bin.html', context)
    else:
        return render(request, 'create_bin.html', context)


class BinCreateView(BaseCreateView):
    model = Bin
    form_class = CreateBinForm
    template = 'create_bin.html'
    success_url = 'index'

    def form_valid(self, form):
        self.model.name = form.cleaned_data['name']
        self.model.ip_address = form.cleaned_data['ip_address']
        self.model.save()
