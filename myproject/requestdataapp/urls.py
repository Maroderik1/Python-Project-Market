from django.urls import path

from .views import process_get_view


app_name = 'requestdataapp'

urlpatterns = [
    path('get/', process_get_view, name='get-view'),
]