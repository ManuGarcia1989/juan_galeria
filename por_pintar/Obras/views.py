from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import Obras


class indexView(ListView):
    model = Obras
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(indexView, self).get_context_data(**kwargs)
        context['obras'] = Obras.objects.all()
        return context