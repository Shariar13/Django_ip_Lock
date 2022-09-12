from ast import Not
from asyncio.windows_events import NULL
from dataclasses import field
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import paragraph
from ipware import get_client_ip
from .forms import ip_form
from django.contrib.auth import authenticate, login, logout


def home(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    context = {}
    if paragraph.objects.filter(user_ip=ip):
        context['paragraph'] = paragraph.objects.filter(user_ip=ip)
        return render(request, 'fixed_paragraph.html', context)
    else:
        context['paragraph'] = paragraph.objects.filter(user_ip__isnull = True).order_by("?")
        return render(request, 'index.html', context)


class generate (UpdateView):
    model = paragraph
    fields = ['user_ip' , 'username']
    template_name = "generate.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        context['ip'] = ip
        return context

