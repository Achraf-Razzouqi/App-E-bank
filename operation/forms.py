from django.forms import ModelForm
from .models import Operation
from django.contrib.auth.forms import UserCreationForm

class OperForm(ModelForm):
    class Meta:
        model = Operation
        fields = ['idD','solde','type']
