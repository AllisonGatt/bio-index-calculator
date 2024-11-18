from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import SampleForm, EditSampleForm, FilterForm
from .models import MacroinvertebrateSample

@login_required
def add_sample(request):
    if request.method == 'POST':
        form = SampleForm(request.POST)
        if form.is_valid():
            sample = form.save(commit=False)
            sample.user = request.user
            sample.save()
            messages.success(request, "Sample added successfully.")
            return redirect('dashboard')
    else:
        form = SampleForm()
    return render(request, 'add_sample.html', {'form': form})

def dashboard(request):
    samples = MacroinvertebrateSample.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'samples': samples})

@login_required
def edit_sample(request, sample_id):
    sample = get_object_or_404(MacroinvertebrateSample, id=sample_id, user=request.user)
    if request.method == 'POST':
        form = EditSampleForm(request.POST, instance=sample)
        if form.is_valid():
            form.save()
            messages.success(request, "Sample updated successfully.")
            return redirect('dashboard')
    else:
        form = EditSampleForm(instance=sample)
    return render(request, 'edit_sample.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('dashboard')
        messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def view_data(request):
    form = FilterForm(request.GET)
    samples = MacroinvertebrateSample.objects.all()

    if form.is_valid():
        region = form.cleaned_data.get('region')
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')

        if region:
            samples = samples.filter(sampling_region__icontains=region)
        if start_date:
            samples = samples.filter(sample_start_date__gte=start_date)
        if end_date:
            samples = samples.filter(sample_end_date__lte=end_date)
    else:
        messages.error(request, "Invalid filter data. Please try again.")
        form = FilterForm()

    return render(request, 'publicdata.html', {'form': form, 'samples': samples})
