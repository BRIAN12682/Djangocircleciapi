from django.db import models

# Create your models here.
class LibralianModel(models.Model):
    admin_id = models.IntegerField( primary_key= True,)
    libralian_no = models.IntegerField()
    admin_name= models.CharField(max_length= 30,)
    admin_password = models.CharField(max_length=50,)
    admin_email = models.EmailField(blank=False)
    active   = models.BooleanField(default=False)
    
    def __str__(self):
        return self.admin_name