from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from Homeapp.models import Books, Borrowedbooks#, Std_users
from Homeapp.forms import Search_form
from django.template import loader
import datetime as dt

from std_app.models import Std_model
# Create your views here.
def denied_access_return(request,std_number,bk_id):
    return HttpResponse("<h2><font color = \"red\" type =\"Tempus sans ITC\"><center>Denied access<br>Onlylibralians can return Books</center></font></h2>")
def denied_access_report(request,std_number):
    return HttpResponse("<h2><font color = \"red\" type =\"Tempus sans ITC\"><center>Denied access<br>Onlylibralians can view reports or add booksadd Books</center></font></h2>")

def std_books_search_veiw(request, std_number ):

    form = Search_form()
    query_set = Books.objects.all()
    if request.method == "POST":
        form = Search_form(request.POST)
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
            # query_set = Books.objects.filter(
            #     request.POST['by']__icontains = request.POST.get('keystrings')
            #     )
    context = {
        'form'       :  form,
        'query_set'  :  query_set,
        "user"       :  std_number,
        "app"    :  "std_app",
    }
    # notify()
    return HttpResponse(render(request, "search.html" ,context))

def borrow_book_view(request , std_number ,bk_id ):
    notify()
    book_being_borrowed = Books.objects.get( id = bk_id )
    borrowing_student = Std_model.objects.get( personal_No = std_number)
    if (not book_being_borrowed.availability):
        return HttpResponse("<h1>Book already Booked or reserved</h1>")
    else:
        try:
            Borrowedbooks(bks_id = book_being_borrowed, std_number = borrowing_student, borrow_date = dt.datetime.now().date()).save()
            try:
                book_being_borrowed.availability = False
                book_being_borrowed.save()
                Borrowedbooks(bks_id = book_being_borrowed, std_number = borrowing_student, borrow_date = dt.datetime.now().date()).save()
            except:
                pass
            return HttpResponse(f"<h1>You have succeesfully borrowed {book_being_borrowed.book_title}</h1>")
        except:
            return HttpResponse("<h1>One can only borrow one book at time</h1>")
    
    
    #Borrowedbooks.objects.create(bks_id = bk_id, std_number = std_number, borrow_date = dt.datetime.now().date()).save()
    # template = loader.get_template('''template.html''')

    # return HttpResponsePermanentRedirect(f"/std_app/{std_number}/")

def notify():
    from Homeapp.models import Borrowedbooks
    from django.core.mail import send_mail
    from django.utils import timezone
    from django.conf import settings
    set = Borrowedbooks.objects.all()
    for x in set:
        subject = f"Notice to return { x.bks_id.book_title }"
        message = f"Dear { x.std_number.stdname }, \nYou are hear by being remindered that you should are left with one day to the return of \n{x.bks_id.book_title}" 
        if timezone.now() == (x.borrow_date + timezone.timedelta(days = 2)):
            send_mail(subject, message, settings.EMAIL_HOST_USER, [x.std_number.email,])
    print ("notify me please")
