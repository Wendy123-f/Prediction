from django import forms 
from .models import Plagiarism

class PlagiarismModelForm(forms.ModelForm):
    class Meta:
        model = Plagiarism
        fields = ['text']