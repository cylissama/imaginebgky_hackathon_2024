from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'points-of-interest', PointOfInterestViewSet)
router.register(r'routes', RouteViewSet)


urlpatterns = [
    path('', home_view, name='home'),
    path('api/', include(router.urls)),
    path('complaints/', complaint_view, name="complaints"),
    path('map/', map_view, name='map_view'),
    path('pass/', pass_view, name='pass_view')
]


