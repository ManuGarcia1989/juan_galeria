from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import *


class indexView(ListView):
    model = Obras
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(indexView, self).get_context_data(**kwargs)
        context['obras'] = Obras.objects.all()
        context['lights'] = Lights.objects.all()
        context['scene'] = Scene.objects.get(active=True)
        return context
