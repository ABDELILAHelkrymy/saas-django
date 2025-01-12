from django.http import HttpResponse
from django.shortcuts import render

def home_page_view(request, *args, **kwargs):
    var = 'Hello World'
    context = {
        'title': 'home',
    }
    return render(request, 'home.html' , context)