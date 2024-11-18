from django import forms
from .models import MacroinvertebrateSample
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class SampleForm(forms.ModelForm):
    class Meta:
        model = MacroinvertebrateSample
        fields = [
            'ephemeroptera',
            'plecoptera',
            'trichoptera',
            'total_sampled',
            'sample_start_date',
            'sample_end_date',
            'sampling_region'
        ]
        widgets = {
            'sample_start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'sample_end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'sampling_region': forms.TextInput(attrs={'placeholder': 'Region', 'class': 'form-control'}),
        }
        labels = {
            'ephemeroptera': 'Ephemeroptera Count',
            'plecoptera': 'Plecoptera Count',
            'trichoptera': 'Trichoptera Count',
            'total_sampled': 'Total Number of Macroinvertebrates Sampled',
            'sample_start_date': 'Sampling Start Date',
            'sample_end_date': 'Sampling End Date',
            'sampling_region': 'Sampling Region',
        }
        help_texts = {
            'total_sampled': 'Enter the total number of macroinvertebrates collected in the sample.',
            'sampling_region': 'Specify the region where sampling was conducted (e.g., Great Lakes).',
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('sample_start_date')
        end_date = cleaned_data.get('sample_end_date')

        if start_date and end_date and start_date > end_date:
            self.add_error('sample_start_date', "Start date mus
