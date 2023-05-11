from django import forms
from django.forms import ModelForm, Form

from Homeapp.models import Books
choice = ["book_title", "author", "availability", "subject_area"]
class Search_form( Form ):
    by = forms.CharField(
        max_length = 50, 
        required = True,        
        widget= forms.TextInput( 
            attrs= {
                "placeholder":"Seacrh by",
                "name"       :"By",
                "choice"     :choice
                }
            )
        )
    your_search = forms.CharField( 
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder":"keystrings"
                    }
                )
        )


    def clean_by(self, *args, **kwargs):
        by = self.cleaned_data.get("by")
        if by not in ("book_title", "author", "availability","subject_area"):
            raise forms.ValidationError("Can only search under: book_title, author, availability, subject_area")

    def clean_your_search(self, *args, **kwargs):
        your_search = self.cleaned_data.get("your_search")
        by = self.cleaned_data.get("by")
        if ((by == "availability") and (your_search in (0,1))):
            raise forms.ValidationError("for \"availability\" only use \"1\" and \"0\" for \"True\" and \"False\" respectively ")
        else:
            #raise forms.ValidationError("for \"availability\" only use \"1\" and \"0\" for \"True\" and \"False\" respectively ")
            pass


class Bookform( ModelForm ):
    publication_date    = forms.DateField( 
    widget=forms.TextInput(
        attrs={
            "placeholder":"mm/dd/yyyy"
            }
        )
    )
    class Meta:
        model = Books
        exclude = [ ]