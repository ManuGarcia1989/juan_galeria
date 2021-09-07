from django.contrib import admin

# Register your models here.
from .models import *

class ObraAdmin(admin.ModelAdmin):
    list_display = ['title','price']
    search_fields = ['title','price']

class LightAdmin(admin.ModelAdmin):
    list_display = ['type', 'intensity','position']
    search_fields = ['type', 'intensity','position']

class SceneAdmin(admin.ModelAdmin):
    list_display = ['name','active']
    search_fields = ['name','active']

class ObjectGltfAdmin(admin.ModelAdmin):
    list_display = ['name','active']
    search_fields = ['name','active']

admin.site.register(Obra, ObraAdmin)
admin.site.register(Light, LightAdmin)
admin.site.register(Scene, SceneAdmin)
admin.site.register(ObjectGltf, ObjectGltfAdmin)