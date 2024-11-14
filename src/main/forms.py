from django import forms
from .models import MacroinvertebrateSample

class SampleForm(forms.ModelForm):
    class Meta:
        model = MacroinvertebrateSample
        fields = ['ephemeroptera', 'plecoptera', 'trichoptera', 'total_sampled', 'sample_start_date', 'sample_end_date', 'sampling_region']
