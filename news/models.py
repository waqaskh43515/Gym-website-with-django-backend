from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField



class News(models.Model):
    Name = models.CharField(max_length=255)
    Message = HTMLField()

# Create your models here.
    new_name = AutoSlugField(populate_from='Name', unique=True,null=True,default=None)
    new_image = models.FileField(upload_to='news/',max_length=255,null=True,blank=True)
