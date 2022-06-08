from dataclasses import field, fields
from django import forms
from .models import *

class pcForm(forms.ModelForm):
    class Meta:
        model = PC
        fields = "__all__"