from logging import PlaceHolder
from django.forms import CharField, ModelForm, PasswordInput
from .models import LibralianModel

class LibralianSignupForm(ModelForm):
    class Meta:
        model = LibralianModel
        fields = [ 'libralian_no','admin_name','admin_email','admin_password']

class LibralianLoginForm(ModelForm):
    admin_password = CharField(widget=PasswordInput(
            attrs={
                "placeholder" : "Your password"
            }
            )
        )
    class Meta:
        model = LibralianModel
        fields = ['admin_name','admin_password']