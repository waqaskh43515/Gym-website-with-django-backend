from django.db import models


class Contactenquiry(models.Model):
    Name = models.CharField(max_length=255)
    Phone = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Message = models.TextField()



# Create your models here.
