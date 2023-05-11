from django.contrib import admin
from .models import Books,Borrowedbooks
# Register your models here.
admin.site.register(Books)
admin.site.register(Borrowedbooks)