from django.db import models
from autoslug import AutoSlugField
# Create your models here.


class Videos(models.Model):
    Name = models.CharField(max_length=255)
    Message = models.TextField()


    
