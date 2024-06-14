from django import forms
from .models import Submission
from django.contrib.auth.models import User

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['assignment', 'file']

class student_regform(forms.ModelForm):
    class Meta:
        model = User
        fields =["username","first_name","last_name","email","password"]
        
class student_loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField()