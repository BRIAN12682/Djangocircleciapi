from django import forms
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from std_app.forms import StudentSignUpForm, StudentLoginForm
from std_app.models import Std_model
from std_app.views import std_books_search_veiw
from libralian.forms import LibralianSignupForm, LibralianLoginForm
from libralian.models import LibralianModel
from libralian.views import find_book_view
from django.urls import reverse
from libralian.views import find_book_view
# Create your views here.
def home_view(request):
    #template = loader.get_template ("test.html")
    return render(request, "Home.html", {})

def student_view( request,):
    template = loader.get_template ("student.html")
    return HttpResponse(template.render({}, request))

def libralian_view(request,):
    template = loader.get_template ("libralian.html")
    return HttpResponse(template.render())

def std_login_view(request,):
    form = StudentLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("stdname")
        stdrecord = get_object_or_404(Std_model, stdname = username)
        if (stdrecord.password == form.cleaned_data.get("password") and stdrecord.active):
            return HttpResponsePermanentRedirect(f"/std_app/{stdrecord.personal_No}/")
        else:
            return HttpResponse(
                "<center>invalid user<br> try again<br>or try account's registration/activation <br>here<a href = \"../std_signup/\">Sign up</a></center>"
                )

    context = {
        "form" : form
    }
    template = loader.get_template ("studentlogin.html")
    return HttpResponse(template.render(context, request))

def libralian_login_view(request,):
    form = LibralianLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("admin_name")
        adminrecord = get_object_or_404(LibralianModel, admin_name = username)
        if (adminrecord.admin_password == form.cleaned_data.get("admin_password") and adminrecord.active):
            return HttpResponsePermanentRedirect(f"/libralian/{adminrecord.admin_id}/")
        else:
            return HttpResponse(
                "<center>invalid user<br> try again<br>or try account's registration/activation <br>here<a href = \"../libralian_signup/\">Sign up</a></center>"
                )
        #find_book_view( request, adminrecord.admin_id)

    context = {
        "form" : form
    }
    template = loader.get_template ("libralianlogin.html")
    return HttpResponse(template.render(context, request))

def std_signup_view(request):
    form = StudentSignUpForm()
    if request.method == "POST":
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data
            b = get_object_or_404(Std_model, stdname = a["stdname"] )
            if (a["std_personal_No"] == b.personal_No and a["email"] == b.email and a["stdname"] == b.stdname):
                if (b.active != True):
                    b.active = True
                else:
                    return HttpResponse("<p><h1>your account is already active</h1><br>try logging in.<p>")
                b.std_personal_No =a["std_personal_No"]
                b.password = a["password"]
                b.save()
            else:
                return HttpResponse("<p><h1>There is no record of you in our system.</h1><br>Please check your data entry carefully</p>")
    form = StudentSignUpForm()
    context = {
        "form" : form
    }
    template = loader.get_template ("StudentSignUp.html")
    return HttpResponse(template.render(context, request)) 

def libralian_signup_view(request):
    form = LibralianSignupForm()
    if request.method == "POST":
        form = LibralianSignupForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data
            b = get_object_or_404(LibralianModel, admin_id = a["libralian_no"])
            if(a["admin_name"] == b.admin_name and a["libralian_no"]==b.admin_id and b.admin_email == a["admin_email"]):
                if (b.active != True):
                    b.active = True
                else: 
                    return HttpResponse("<p><h1>your account is already active</h1><br>try logging in.<p>")
                b.admin_password = a["admin_password"]
                b.libralian_no = a["libralian_no"]
                b.save()
            else:
                return HttpResponse("<p><h1>There is no record of you in our system.</h1><br>Please check your data entry carefully</p>")
    form = LibralianSignupForm()
    context = {
        "form" : form
    }
    template = loader.get_template ("libralianSignUp.html")
    return HttpResponse(template.render(context, request))  