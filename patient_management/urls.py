from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from patients.api import PatientViewSet

router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # ✅ Add this line
]
