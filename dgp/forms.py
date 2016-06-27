from django import forms

from .models import Run
from .choices import *

class RunForm(forms.ModelForm):

    target = forms.CharField(label='Cible')
    typeCol = forms.ChoiceField(choices = TYPE_CHOICES, label='Type de collectivité')

    class Meta:
        model = Run
        fields = ('target','typeCol')
