from django import forms
from django.conf import settings

#import os #for splitext
#import re

class AddURLForm(forms.Form):
    url = forms.URLField(label='Craigslist URL')

