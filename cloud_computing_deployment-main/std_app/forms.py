from django.forms import CharField, ModelForm, PasswordInput
from .models import Std_model

class StudentSignUpForm(ModelForm):
    class Meta:
        model = Std_model
        fields = ['stdname','std_personal_No','email','password']

class StudentLoginForm(ModelForm):
    password = CharField(
        widget = PasswordInput(
            attrs={
                "placeholder":"your password"
            }
        )
    )
    class Meta:
        model = Std_model
        fields = ['stdname','password']