from django import forms
from input_hidden_multi_forms.models import Hidden

class HiddenForm(forms.ModelForm):
    HIDDEN_LIST = (
        'Item 01',
        'Item 02',
        'Item 03',
        'Item 04',
        'Item 05',
        'Item 06',
        
    )
    dado = forms.CharField(widget=forms.MultipleHiddenInput(), initial=HIDDEN_LIST)
    class Meta:
        model = Hidden
        fields = ('nome', 'dado')