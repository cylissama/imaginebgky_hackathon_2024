from django.db import models

class Complaint(models.Model):
    # Auto-increment ID field is added automatically by Django as the primary key
    filer_name = models.CharField(max_length=100, verbose_name="Filer Name")
    email_address = models.EmailField(verbose_name="Email Address")
    phone_number = models.CharField(max_length=20, verbose_name="Phone Number")
    reason_for_complaint = models.TextField(verbose_name="Reason for Complaint")

    def __str__(self):
        return f"Complaint by {self.filer_name}"

class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name