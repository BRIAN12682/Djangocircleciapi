from email.policy import default
# from typing_extensions import Required
from django.db import models
from django.utils import timezone
from std_app.models import Std_model
import datetime as dt

# Create your models here.
class Books(models.Model):
    id               = models.AutoField( primary_key= True )
    book_title       = models.CharField( max_length= 70 )
    publication_date = models.DateField('publication date')
    subject_area     = models.CharField( max_length= 70 )
    author           = models.CharField( max_length= 40 )
    availability     = models.BooleanField( default=False )
    
    def __str__(self):
        return self.book_title

class Borrowedbooks(models.Model):
    bks_id       = models.OneToOneField(Books, related_name="bookid", on_delete=models.CASCADE)
    std_number  = models.OneToOneField(Std_model,related_name="stdNumber", on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add= True,)

    def __str__(self):
        return self.bks_id

    # def notify(self,*args,**kwargs):
    #     pass
    
    def penalty (self,*args,**kwargs):
        ten_days = (self.borrow_date + timezone.timedelta( days = 10))
        five_days = (self.borrow_date + timezone.timedelta( days = 5))
        now_date = dt.datetime.now().date()
        if (now_date >= ten_days):
            return "Ushs 15000"
        elif( now_date>=five_days ):
            return "Ushs 5000"
        else:
            return "Ushs 0"
            
    def return_date(self,*args,**kwargs):
        return self.borrow_date + timezone.timedelta(days = 3)