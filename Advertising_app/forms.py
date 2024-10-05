from django import forms
from .models import Advertising

class IrisFlowerForm(forms.ModelForm):
    class Meta:
        model = Advertising
        fields = ['TV', 'Radio', 'Newspaper']
        widgets = {
            'TV': forms.NumberInput(attrs={'placeholder': 'TV'}),
            'Radio': forms.NumberInput(attrs={'placeholder': 'Radio'}),
            'Newspaper': forms.NumberInput(attrs={'placeholder': 'Newspaper'}),
        }