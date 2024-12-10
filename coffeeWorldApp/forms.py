from django import forms
from .models import Drink, Bean

class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = ('name', 'ingredients')

class BeanForm(forms.ModelForm):
    class Meta:
        model = Bean
        fields = ('country', 'name')
        