from django import forms

from .models import Run
from .choices import *

class RunSelectionForm(forms.ModelForm):

    platform = forms.ChoiceField(choices = PLATFORM_CHOICES,label='Plateforme')
    target = forms.ChoiceField(choices = TARGET_CHOICES,label='Cible')
    typeCol = forms.ChoiceField(choices = TYPE_CHOICES, label='Type de collectivité')

    class Meta:
        model = Run
        fields = ('platform','target','typeCol')

class RunParametersForm(forms.ModelForm):

    platform = forms.ChoiceField(choices = PLATFORM_CHOICES,label='Plateforme')
    target = forms.CharField(label='Cible')
    username = forms.CharField(label='Utilisateur')
    password = forms.CharField(label='Mot de passe')
    typeCol = forms.ChoiceField(choices = TYPE_CHOICES, label='Type de collectivité')

    class Meta:
        model = Run
        fields = ('platform','target','username','password','typeCol')
