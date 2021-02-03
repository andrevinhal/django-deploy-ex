from django.urls import path
from BasicApp import views

app_name = 'basic_app'

urlpatterns = [
    path('relative/',views.rel_url_temps,name='relative'),
    path('other/',views.other,name='other'),
]