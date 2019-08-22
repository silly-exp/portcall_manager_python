from django import forms
from .fields import ImoField


class CallForm(forms.Form):
    locode = forms.CharField(label='Locode du port', max_length=5, min_length=5)
    imo = ImoField(label='OMI du navire')
    eta_date = forms.DateTimeField(label='ETA day', widget=forms.DateInput(attrs={'type':'date'}))
    eta_time = forms.TimeField(label='ETA time', widget=forms.TimeInput(attrs={'type':'time'}))
    etd_date = forms.DateTimeField(label='ETD day', widget=forms.DateInput(attrs={'type':'date'}), required=False)
    etd_time = forms.TimeField(label='ETD time', widget=forms.TimeInput(attrs={'type':'time'}), required=False)

    """
    https://docs.djangoproject.com/fr/2.1/ref/forms/validation/

    les widget DateInput, TimeInput et DateTimeInput sont en fait de simples champs text.
    https://stackoverflow.com/questions/42623490/datetimefield-displaying-a-textbox-instead-of-a-date-picker
    3 solutions:
    - ajouter un type html5 dans attrs: fonctionne en fonction des navigateurs...
    - ajouter un composant js à la main.
    - utiliser une extension django

    Il est certain que je ne peux pas simplement saisir les champs du modèle dans le formulaire
    - je ne peux pas demander l'id des objets liés comme le port ou le navire
    - je ne peux pas demander la date et l'heure dans un seul champ
    """



class HomeForm(forms.Form):
    locode = forms.CharField(label='Locode du port', max_length=5, min_length=5)
