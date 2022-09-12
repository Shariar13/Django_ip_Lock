from django import forms
from .models import paragraph
class ip_form(forms.ModelForm):
    class Meta:
        model = paragraph
        fields = ( 'user_ip',)