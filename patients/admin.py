from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    # Columns to display in the admin list view
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'created_at')

    # Fields you can search for in the search bar
    search_fields = ('first_name', 'last_name', 'email')

    # Filters that appear on the right-hand side
    list_filter = ('date_of_birth', 'created_at')

