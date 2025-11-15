from django import forms
from .models import Wish

class WishForm(forms.ModelForm):
    class Meta:
        model = Wish
        fields = ['name', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Your name (optional)'}),
            'message': forms.Textarea(attrs={'placeholder':'Write a wish for Sita...','rows':3}),
        }
