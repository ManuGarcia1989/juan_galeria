from django.db import models

# Create your models here.
class Obra(models.Model):
    model = models.FileField(upload_to="objects3D/")
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="imagenesGafas/")
    dimentions = models.CharField(max_length=150)
    date = models.DateField(verbose_name="Date Pices")
    price = models.CharField(max_length=150 )
    checkpoint = models.CharField(max_length=150, help_text = "Donde va a teletransportarse el observador ex:0 0 0")
    position = models.CharField(max_length=150, help_text = "0 0 0")
    rotation = models.CharField(max_length=150, help_text = "0 0 0")
    scale = models.CharField(max_length=150, help_text = "0 0 0")

class Light(models.Model):
    color = models.CharField(max_length=150, help_text="#FFF")
    type = models.CharField(max_length=150, help_text="One of ambient, directional, hemisphere, point, spot.")
    intensity = models.FloatField(verbose_name="Intensity")
    position = models.CharField(max_length=150, help_text="0 0 0")
    rotation = models.CharField(max_length=150, help_text="0 0 0")

class Scene(models.Model):
    name = models.CharField(max_length=150,verbose_name="Scene Name")
    model = models.FileField(upload_to="objects3D/scenes/")
    active = models.BooleanField(default=False, verbose_name="Active Scene")

class ObjectGltf(models.Model):
    name = models.CharField(max_length=150,verbose_name="Object")
    model = models.FileField(upload_to="objects3D/object/")
    active = models.BooleanField(default=False, verbose_name="Active Object")
    position = models.CharField(max_length=150, help_text="0 0 0")
    rotation = models.CharField(max_length=150, help_text="0 0 0")
    scale = models.CharField(max_length=150, help_text="0 0 0")
