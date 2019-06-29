from django import forms
from .models import TutorApply, TutorRequest

class TutorApplyForm(forms.ModelForm):
    class Meta:
        model = TutorApply
        fields = ('title', 'content', 'image')

class TutorRequestForm(forms.ModelForm):
    class Meta:
        model = TutorRequest
        fields = ('title', 'content', 'image')