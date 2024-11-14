

from django.shortcuts import render, redirect
from .forms import SampleForm
from django.contrib.auth.decorators import login_required

@login_required
def add_sample(request):
    if request.method == 'POST':
        form = SampleForm(request.POST)
        if form.is_valid():
            sample = form.save(commit=False)
            sample.user = request.user
            sample.save()
            return redirect('dashboard')
    else:
        form = SampleForm()
    return render(request, 'add_sample.html', {'form': form})

# main_app/views.py

def dashboard(request):
    return render(request, 'templates/dashboard.html')

def edit(request):
    return render(request, 'main_app/edit.html')

def add_sample(request):
    return render(request, 'main_app/add_sample.html')

def view_data(request):
    return render(request, 'main_app/view_data.html')
