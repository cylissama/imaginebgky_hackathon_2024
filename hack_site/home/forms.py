from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['filer_name', 'email_address', 'phone_number', 'reason_for_complaint']
