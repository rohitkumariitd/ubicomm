from django.shortcuts import render
from django.views import generic
from .models import UbicInstance
# Create your views here.
class DetailView(generic.DetailView):
    model = UbicInstance
    template_name = 'ubic/main.html'
