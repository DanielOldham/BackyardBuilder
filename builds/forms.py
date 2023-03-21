from django import forms
from .models import Build


class BuildNameForm(forms.ModelForm):
    """
    Django ModelForm.
    Allows setting of the Build Model name.
    """

    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        """
        Django Meta inner class.
        """

        model = Build
        fields = ['name']
