from django.contrib import admin
from .models import MacroinvertebrateSample, Sample

# Customize MacroinvertebrateSample display
class MacroinvertebrateSampleAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'ephemeroptera', 'plecoptera', 'trichoptera', 
                    'total_sampled', 'EPT_index', 'sampling_region', 
                    'sample_start_date', 'sample_end_date')
    list_filter = ('user', 'sampling_region', 'sample_start_date', 'sample_end_date')
    search_fields = ('user__username', 'sampling_region')
    ordering = ('-sample_start_date',)
    readonly_fields = ('EPT_index',)

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'User'

admin.site.register(MacroinvertebrateSample, MacroinvertebrateSampleAdmin)

# Customize Sample display
class SampleAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'taxa', 'location', 'date_collected')
    list_filter = ('user', 'location', 'date_collected')
    search_fields = ('user__username', 'taxa', 'location')

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'User'

admin.site.register(Sample, SampleAdmin)
