from django.shortcuts import render
from django.views.generic import ListView
from measurements.models import Area
# Create your views here.

class AreaView(ListView):
    """
        Using Django generic view for listing rows of model Area in template named Final.html
    """
    model = Area
    template_name = 'Final.html'
    context_object_name = 'areas'

