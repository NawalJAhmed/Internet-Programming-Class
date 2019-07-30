from django.contrib import admin
from measurements.models import Category, Location, Area, Measurement
# Register your models here.


class LocationInline(admin.TabularInline):
    """
        Help to create a table like view for Location model
    """
    model = Location

class AreaAdmin(admin.ModelAdmin):
    """
        Add tabular view of Location to Area fields in the admin
    """
    inlines = [
        LocationInline,
    ]

class MeasurementInline(admin.TabularInline):
    """
        Help to create a table like view for Measurement model
    """
    model = Measurement

class LocationAdmin(admin.ModelAdmin):
    """
        Add tabular view of Measurement to Location fields in the admin
    """
    inlines = [
        MeasurementInline,
    ]

class CategoryAdmin(admin.ModelAdmin):
    """
        Display a vertical type view for choosing members
    """
    filter_vertical = ('members',)

# Register Admin configurations with the model
admin.site.register(Area, AreaAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)