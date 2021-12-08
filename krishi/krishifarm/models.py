from django.db import models
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=70)
    tractor = models.CharField(max_length=70)
    model_number = models.CharField(max_length=70,null=False, blank=False)
    implements = models.CharField(max_length = 255,blank=True,null=True )
