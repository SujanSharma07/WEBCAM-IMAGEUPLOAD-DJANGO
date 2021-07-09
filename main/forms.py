from django import forms
from .models import *


class TreeLeafForm(forms.ModelForm):
    class Meta:
        model = TreeLeaf
        fields = '__all__'
