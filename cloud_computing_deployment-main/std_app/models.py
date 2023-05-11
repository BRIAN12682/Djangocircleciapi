from django.db import models

# Create your models here.
class Std_model(models.Model):
    personal_No = models.IntegerField(primary_key=True )
    std_personal_No = models.IntegerField()
    stdname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(blank= True, max_length=50)
    active   = models.BooleanField(default=False)
    