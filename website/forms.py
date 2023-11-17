from django import forms

from .models import ContactModel

class MyModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['username', 'user_email', 'Phone_no' ,'email_subject', 'email_message']
   