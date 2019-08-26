from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView

from .models import CreateEvent, Carosoul, Gallery, Testimonials,Companies
from .forms import CreateEventForm

def render_test_view(request):
    return render(request,'base.html')

# Generic views
class HomeCreateView(CreateView):
    model=CreateEvent
    template_name = 'pages/home.html'
    form_class = CreateEventForm

    def get_carosoul_details(self):
        #ToDo: Optimise below code
        return Carosoul.objects.all()[0:3]

    def get_gallery_details(self):
        #ToDo: Optimise below code
        return Gallery.objects.all()[0:10]

    def get_testimonial_details(self):
        #ToDo: optimise below code
        return Testimonials.objects.all()[0:3]

    def get_company_details(self):
        #ToDo: optimise below code
        return Companies.objects.all()[0:10]

class EventManagementCreateView(CreateView):
    model=CreateEvent
    template_name = 'pages/event_management.html'
    form_class = CreateEventForm



class OurEventsCreateView(CreateView):
    pass


# Form views
class CreateEventFormView(FormView):
    template_name = 'create_event_form.html'
    form_class = CreateEventForm
    success_url = '/'
