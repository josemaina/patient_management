from django.contrib import admin
from django.urls import path, include
from patients.views import home
from rest_framework import routers
from patients.api import PatientViewSet  # if you have API endpoints

# Create DRF router
router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet)

urlpatterns = [
     path('', include('patients.urls')),
    path('', home, name='home'),          # Home page
    path('admin/', admin.site.urls),      # Admin panel
    path('api/', include(router.urls)),   # API endpoints
    path('', include('patients.urls')),
]

