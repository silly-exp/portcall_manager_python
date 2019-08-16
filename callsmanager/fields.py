from django import forms
from .validators import validate_IMO

class ImoField(forms.IntegerField):
    default_validators=[validate_IMO]
