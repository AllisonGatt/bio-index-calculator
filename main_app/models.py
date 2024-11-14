from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class MacroinvertebrateSample(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ephemeroptera = models.PositiveIntegerField()
    plecoptera = models.PositiveIntegerField()
    trichoptera = models.PositiveIntegerField()
    total_sampled = models.PositiveIntegerField()
    sample_start_date = models.DateField()
    sample_end_date = models.DateField()
    sampling_region = models.CharField(max_length=100)
    EPT_index = models.FloatField(blank=True, null=True)

#ADDED AN ELSE TO HANDLE IF THERE ARE NO ORGANISMS SAMPLED
    def calculate_ept_index(self):
        total_ept = self.ephemeroptera + self.plecoptera + self.trichoptera
        if self.total_sampled > 0:
            return (total_ept / self.total_sampled) * 100
        else:
            raise ValidationError("Total sampled must be more than 0.")

    def save(self, *args, **kwargs):
        # Calculate EPT index before saving
        self.EPT_index = self.calculate_ept_index()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Sample by {self.user.username} - EPT Index: {self.EPT_index:.2f}"
