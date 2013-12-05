from django import forms
#from models import models
from .models import UrlChecker

class UrlCheckerForm(forms.ModelForm):
    class Meta:
        model = UrlChecker
        exclude = ('from_address', 'url_output', 'html_output', )
        