from django.shortcuts import render, redirect
from .models import Complaint 
from .forms import *

def home_view(request):
    return render(request, 'home/index.html')

def complaint_view(request):
    template = 'home/complaints.html'
    context = {}
    complaints = Complaint.objects.all()
    context['complaints'] = complaints
    form = ComplaintForm()

    if request.method == 'POST':
        form = ComplaintForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('complaints')  # Redirect to a new URL after posting
    else:
        form = ComplaintForm()  # An empty form instance for GET request

    context['form'] = form

    return render(request, template, context)
    
