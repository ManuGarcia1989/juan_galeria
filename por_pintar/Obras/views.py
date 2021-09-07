from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import *


class indexView(ListView):
    model = Obra
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(indexView, self).get_context_data(**kwargs)
        context['obras'] = Obra.objects.all()
        context['lights'] = Light.objects.all()
        context['scene'] = Scene.objects.get(active=True)
        context['objects_gltf'] = ObjectGltf.objects.filter(active=True)
        return context
