from django import forms
from . validators import validate_IMO


class CallForm(forms.Form):
    locode = forms.CharField(label='Locode du port', max_length=5, min_length=5)
    imo = forms.IntegerField(label='OMI du navire', validators=[validate_IMO])
    eta = forms.DateTimeField(label='ETA')
    etd = forms.DateTimeField(label='ETD')



class HomeForm(forms.Form):
    pass