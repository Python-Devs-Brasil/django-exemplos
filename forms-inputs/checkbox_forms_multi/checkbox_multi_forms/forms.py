from django import forms
from checkbox_multi_forms.models import CheckBox

class CheckboxForm(forms.ModelForm):
    CHECKBOX_LIST = (
        ('i1', 'Item 01'),
        ('i2', 'Item 02'),
        ('i3', 'Item 03'),
    )
    tipo = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CHECKBOX_LIST )
    
    class Meta:
        model = CheckBox
        fields = ('tipo',)