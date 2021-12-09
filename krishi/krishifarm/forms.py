from django.core import validators
from django import forms
from django.core import validators
from .models import User

class registration(forms.ModelForm):
    class Meta:
        model  = User
        fields = ['name', 'email', 'password', 'tractor','model_number','implements']
        labels = {
            "name" :"Farmer's Name",
            "email" :"Email",
            "password" :"Password",
            "tractor" :"Tractor",
            "model_number" :"Model Number"
            
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'password' : forms.PasswordInput(render_value = True, attrs={'class': 'form-control'}),
            'tractor' : forms.TextInput(attrs={'class': 'form-control'}),
            'model_number' : forms.TextInput( attrs={'class': 'form-control'}),
        }

    IMPLEMENTS = (
        ('Harrow', 'Harrow'),
        ('Cultivator', 'Cultivator'),
        ('Roravator', 'Roravator'),
        ('Plough', 'Plough'),
        ('Paddy Thrasher', 'Paddy Thrasher'),
        ('Dumping Trailer', 'Dumping Trailer'),
        ('4 Wheel Trailer', '4 Wheel Trailer'),
    )


    implements = forms.MultipleChoiceField(
            widget = forms.CheckboxSelectMultiple,
            choices = IMPLEMENTS,
            required = False
    )
