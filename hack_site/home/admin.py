from django.contrib import admin
from .models import Complaint, PointOfInterest

admin.site.register(Complaint)
admin.site.register(PointOfInterest)