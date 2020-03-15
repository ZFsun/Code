from django.contrib import admin
from datademo.models import *

# Register your models here.

admin.sites.site.site_header = 'header_test'
admin.site.site_title = 'title_test'

admin.sites.site.register(Dataset)


# admin.sites.site.register(Statistics)


class DatasetAdmin(admin.ModelAdmin):
    list_display = ('path',)


@admin.register(Statistics)
class Statistics(admin.ModelAdmin):
    list_display = (
        'dawn_num', 'day_num', 'dusk_num', 'night_num', 'sunny_num', 'rain_num', 'overcast_num', 'cloudy_num',
        'urban_num',
        'hightway_num', 'parking_num', 'othersway_num')
