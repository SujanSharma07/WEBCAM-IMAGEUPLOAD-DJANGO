from django.db import models

# Create your models here.


def getcurrentusername(instance, filename):
    return "{0}/{1}".format(instance.name, filename)


class TreeLeaf(models.Model):
    name = models.CharField(max_length=150)
    files = models.FileField(upload_to=getcurrentusername)
    image = models.ImageField(upload_to=getcurrentusername)
