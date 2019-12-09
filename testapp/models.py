from django.db import models

# Create your models here.
from django.conf import settings
from django.core.files.storage import FileSystemStorage
private_storage = FileSystemStorage(location=settings.PRIVATE_STORAGE_ROOT)
import os




class Report(models.Model):
    sheet_name = models.CharField(max_length=32,null=True,blank=True)
    column = models.IntegerField(null=True, blank=True)
    file = models.FileField(storage=private_storage,null=True,blank=True)



class Alpha(models.Model):
    letter  = models.CharField(max_length=32,  null=True, blank=True)
    number = models.IntegerField(null=True,blank=True)




