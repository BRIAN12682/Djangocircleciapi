from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from Homeapp.models import Books, Borrowedbooks
from Homeapp.forms import Search_form , Bookform
from django.template import loader
import datetime as dt
import json


# Create your views here.

def borrow_book_view( request, std_number, bk_id ):
        return HttpResponse(
            "<h2><font color = \"red\" type =\"Tempus sans ITC\"><center>Denied access<br>libralian cant borrow books</center></font></h2>"
            )
        

def find_book_view( request, admin_id ):
    query_set = Books.objects.all()
    form  = Search_form()
    if request.method == "POST":
        form  = Search_form( request.POST )
        if form.is_valid():
            if (request.POST['by'] == "book_title"):
                query_set = Books.objects.filter(
                book_title__icontains = request.POST.get('your_search')
                )
            elif(request.POST['by'] == "author"):
                query_set = Books.objects.filter(
                author__icontains = request.POST.get('your_search')
                )
            elif(request.POST['by'] =="subject_area"):
                query_set = Books.objects.filter(
                subject_area__icontains = request.POST.get('your_search')
                )
            elif(request.POST['by']=="availability"):
                query_set = Books.objects.filter(
                availability__icontains = request.POST.get('your_search')
                )
            
    context = {
        'form'    : form,
        'query_set' : query_set,
        "user": admin_id,
        "app" : "libralian"
    }
    return HttpResponse( render( request, "search.html" , context ))


def return_book_veiw( request, admin_id, bk_id ):
        returnedbook = get_object_or_404(Books, id = bk_id )
        returnedbook.availability = True
        returnedbook.save()
        try:
            Borrowedbooks.objects.get(bks_id = bk_id).delete()
            return HttpResponse(f"<h1>{returnedbook.book_title} has succesfully been returned</h1>")
        except:
            return HttpResponse(f"<h2><center>Book <h4>{returnedbook.book_title}<h4> was already returned.</center></h2>")
        return HttpResponseRedirect(f"/libralian/{admin_id}/")
        
def add_book_veiw (request, admin_id):
    form = Bookform()
    if request.method == "POST":
        form = Bookform( request.POST)
        if form.is_valid():
            form.save()
            form = Bookform()

    template = loader.get_template("add_book.html")
    context = {
        "form" : form
    }
    return HttpResponse(template.render(context, request))

def report_view(request, admin_id):
    obj = Borrowedbooks.objects.all()
    context = {
        "borrowed_bks" : obj,
        "tendays"    : dt.timedelta( days = 10),
        "fivedays"   : dt.timedelta( days = 5),
        "threedays"  : dt.timedelta( days = 3),
         "nowdate"   : dt.datetime.now().date(),
    }
    template = loader.get_template("report.html")
    return HttpResponse(template.render(context, request))