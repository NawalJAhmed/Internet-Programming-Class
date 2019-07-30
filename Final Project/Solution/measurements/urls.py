from django.urls import path
from measurements import views

urlpatterns = [
    path('', views.AreaView.as_view(), name='final'),
]
