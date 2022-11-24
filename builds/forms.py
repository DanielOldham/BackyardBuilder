from django import forms
from .models import Build


class BuildNameForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Build
        fields = ['name']
