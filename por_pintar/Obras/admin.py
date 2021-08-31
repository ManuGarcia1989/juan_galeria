from django.contrib import admin

# Register your models here.
from .models import *

class ObrasAdmin(admin.ModelAdmin):
    list_display = ['title','price']
    search_fields = ['title','price']

class LightsAdmin(admin.ModelAdmin):
    list_display = ['type', 'intensity','position']
    search_fields = ['type', 'intensity','position']

class SceneAdmin(admin.ModelAdmin):
    list_display = ['name','active']
    search_fields = ['name','active']

admin.site.register(Obras, ObrasAdmin)
admin.site.register(Lights, LightsAdmin)
admin.site.register(Scene, SceneAdmin)