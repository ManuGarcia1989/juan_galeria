from django.db import models

# Create your models here.
class Obras(models.Model):
    model = models.FileField(upload_to="objects3D/")
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="imagenesGafas/")
    dimentions = models.CharField(max_length=50)
    date = models.DateField(verbose_name="Date Pices")
    price = models.CharField(max_length=150 )
    position = models.CharField(max_length=12, help_text = "0 0 0")
    rotation = models.CharField(max_length=12, help_text = "0 0 0")
    scale = models.CharField(max_length=12, help_text = "0 0 0")


