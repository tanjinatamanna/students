from django import forms
from .models import CV

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = [
            'full_name', 'email', 'phone', 'address',
            'institution', 'degree', 'passing_year',
            'company', 'role', 'duration', 'description',
            'skills'
        ]
        widgets = {
            'address': forms.Textarea(attrs={'rows':2}),
            'description': forms.Textarea(attrs={'rows':3}),
            'skills': forms.Textarea(attrs={'rows':2}),
        }

