from django.forms import ModelForm,DateField,TextInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field,Row,Column,Div

from . import models

class CreateEventForm(ModelForm):
    class Meta:
        model = models.CreateEvent
        fields = ['first_name','last_name','email','contact_no','category','company_name','date','event_description']

    def __init__(self, *args, **kwargs):

        #Crispy forms configurations
        super(CreateEventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-a'

        #Form attrs configurations
        #Placeholder attr
        self.fields['first_name'].widget.attrs['placeholder'] = 'Your first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Your last name'
        self.fields['email'].widget.attrs['placeholder'] = 'Your email'
        self.fields['contact_no'].widget.attrs['placeholder'] = 'Your contact no'
        self.fields['company_name'].widget.attrs['placeholder'] = 'Your company name'
        self.fields['event_description'].widget.attrs['placeholder'] = 'Describe your event'

        #Type attr
        self.fields['date']= DateField(
            widget= TextInput(
                attrs={'type': 'date'}
            )
        )

        #Css attr
        self.fields['first_name'].widget.attrs['class']='form-control-lg form-control-a'
        self.fields['last_name'].widget.attrs['class']='form-control-lg form-control-a'
        self.fields['email'].widget.attrs['class']='form-control-lg form-control-a'
        self.fields['contact_no'].widget.attrs['class']='form-control-lg form-control-a'
        self.fields['category'].widget.attrs['class']='form-control-lg form-control-a'
        self.fields['company_name'].widget.attrs['class']='form-control-lg form-control-a'
        self.fields['date'].widget.attrs['class']='form-control-lg form-control-a'
        
        

