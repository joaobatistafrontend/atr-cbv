from django import forms

class TestForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    