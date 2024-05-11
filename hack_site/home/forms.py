from django import forms
from .models import *

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['filer_name', 'email_address', 'phone_number', 'reason_for_complaint']

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'categories', 'email', 'phone_number']