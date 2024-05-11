from django.contrib import admin
from .models import *

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('filer_name', 'email_address', 'phone_number', 'reason_for_complaint')

admin.site.register(Category)
admin.site.register(Vendor)
from .models import Complaint, PointOfInterest

admin.site.register(Complaint)
admin.site.register(PointOfInterest)
