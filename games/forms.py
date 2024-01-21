from django import forms
from .models import *

#
# class GameForm(forms.ModelForm):
#     class Meta:
#         model = Game
#         fields = ['name', 'genres', 'platforms',]
#         widgets = {
#             'genres': forms.CheckboxSelectMultiple,
#             'platforms': forms.CheckboxSelectMultiple,
#         }