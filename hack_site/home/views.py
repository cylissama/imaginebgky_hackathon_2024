from django.shortcuts import render, redirect
from .models import * 
from .forms import *
from .serializers import PointOfInterestSerializer, RouteSerializer
from rest_framework import viewsets

def home_view(request):
    template = 'home/index.html'
    context = {}
    vendors = Vendor.objects.all()
    context['vendors'] = vendors
    return render(request, template, context)

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
    
def add_vendor_view(request):
    template = 'home/add_vendors.html'
    context = {}
    form = VendorForm()

    if request.method == 'POST':
        form = VendorForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('vendor')  # Redirect to a new URL after posting
    else:
        form = VendorForm()  # An empty form instance for GET request

    context['form'] = form

    return render(request, template, context)


class PointOfInterestViewSet(viewsets.ModelViewSet):
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerializer

    
class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

def map_view(request):
    points_of_interest = PointOfInterest.objects.all()
    routes = Route.objects.all()
    points_serializer = PointOfInterestSerializer(points_of_interest, many=True)
    routes_serializer = RouteSerializer(routes, many=True)
    context = {
        'points_data': points_serializer.data,
        'routes_data': routes_serializer.data
    }
    return render(request, 'home/map.html', context)  

def pass_view(request):
    template = 'home/new_pass.html'
    context = {}
    passes = Pass.objects.all()
    context['passes'] = passes

    form = PassForm()

    if request.method == 'POST':
        form = PassForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('pass_view')  # Redirect to a new URL after posting
    else:
        form = PassForm()

    context['form'] = form
    
    return render(request, template, context)