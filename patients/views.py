from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Patient
from .forms import PatientForm

# 🏠 Home page — list all patients
def home(request):
    patients = Patient.objects.all().order_by('-created_at')
    return render(request, 'patients/home.html', {'patients': patients})

# ➕ Add a new patient
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PatientForm()
    return render(request, 'patients/add_patient.html', {'form': form})

# ✏️ Edit a patient
def edit_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/edit_patient.html', {'form': form, 'patient': patient})

# ❌ Delete a patient
def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('home')
    return render(request, 'patients/delete_patient.html', {'patient': patient})
