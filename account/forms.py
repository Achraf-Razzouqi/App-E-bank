from django.forms import ModelForm
from .models import Use
from django.contrib.auth.forms import UserCreationForm

class UserFrom(ModelForm):
    class Meta:
        model = Use
        fields = ['nom','prenom','cne','password','type','phone','solde','age','adress']
class AdminFrom(ModelForm):
    class Meta:
        model = Use
        fields = ['nom','prenom','cne','password','phone','solde','age','adress']
class rFrom(ModelForm):
    class Meta:
        model = Use
        fields = ['nom','prenom','cne','password','phone','age','adress']
class tFrom(ModelForm):
    class Meta:
        model = Use
        fields = ['nom','prenom','cne','password','phone','adress']

