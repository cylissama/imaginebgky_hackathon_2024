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

class PassForm(forms.ModelForm):
    class Meta:
        model = Pass
        fields = ['name', 'county']  # 'id' is auto-generated and not included in the form
