from django import forms

from pollsApp.models import Client


class HomeForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = (
            "email",
        )


