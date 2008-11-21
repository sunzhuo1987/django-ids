from django import forms

class TestForm(forms.Form):
    message = forms.CharField(required=True)
    
