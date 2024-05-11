from django.contrib import admin
from .models import *
from .models import Complaint, PointOfInterest

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('filer_name', 'email_address', 'phone_number', 'reason_for_complaint')

admin.site.register(Category)
admin.site.register(Vendor)
admin.site.register(PointOfInterest)
admin.site.register(Pass)
admin.site.register(Route)