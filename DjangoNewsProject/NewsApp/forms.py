from django import forms
from .models import NewsModal

class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsModal
        fields = ['Id', 'Name', 'Description', 'Author', 'Image', 'Source']