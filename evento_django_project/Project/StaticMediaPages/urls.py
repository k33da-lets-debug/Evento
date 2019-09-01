from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import render_test_view,HomeCreateView,CreateEventFormView,EventManagementCreateView,ContactUsView
app_name = 'StaticMediaPages'

urlpatterns = [
    path('', HomeCreateView.as_view(), name='home'),
    path('', CreateEventFormView.as_view(), name='create_event'),
    path('event_management', EventManagementCreateView.as_view(), name='event_management'),
    path('contact_us', ContactUsView.as_view(), name='contact_us'),
]