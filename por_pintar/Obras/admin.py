from django.contrib import admin

# Register your models here.
from .models import Obras


class ObrasAdmin(admin.ModelAdmin):
    list_display = ['title','price']
    search_fields = ['title','price']

admin.site.register(Obras, ObrasAdmin )