from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

# Main Models

class CreateEvent(models.Model):
    # Validations
    name_regex = RegexValidator(regex='([a-zA-Z])\D*([a-zA-Z])$', message="Special characters, numbers and spaces are not allowed.")
    contact_no_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    #Misc
    CATEGORY_CHOICES = (
        ('CORPORATE_EVENT', 'Corporate event'),
        ('WEDDING_PLANNER', 'Wedding planner'),
        ('SOCIAL_EVENT', 'Social event'),
    )
    #Fields
    first_name = models.CharField(validators=[name_regex],max_length=50)
    last_name = models.CharField(validators=[name_regex],max_length=50,blank=True)
    email = models.EmailField(max_length=50)
    contact_no = models.CharField(validators=[contact_no_regex],max_length=17)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    company_name = models.CharField(max_length=100,blank=True)
    date = models.DateTimeField(auto_now=False)
    event_description = models.TextField(max_length=300)

    #ToDo: add query resolved parameter

    def get_absolute_url(self):
        return '/'

class ContactUs(models.Model):
    # Validations
    name_regex = RegexValidator(regex='([a-zA-Z])\D*([a-zA-Z])$', message="Special characters, numbers and spaces are not allowed.")
    contact_no_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    #Misc
    #Fields
    #TODO: Add datetime field to identify when user posted this query also update it in admin.py
    first_name = models.CharField(validators=[name_regex],max_length=50)
    last_name = models.CharField(validators=[name_regex],max_length=50,blank=True)
    email = models.CharField(max_length=50)
    contact_no = models.CharField(validators=[contact_no_regex],max_length=50)
    message = models.TextField(max_length=300)
    
    def get_absolute_url(self):
        return '/'


# User Interface modification models

# Home page
class Carosoul(models.Model):
    #Foreign key with our events
    title=models.CharField(max_length=50,blank=True)
    subtitle=models.CharField(max_length=50,blank=True)
    short_description=models.TextField(max_length=100,blank=True)
    publish=models.BooleanField(default=True)
    publish_date=models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to='carousel/',default='1.0')

class Gallery(models.Model):
    publish=models.BooleanField(default=True)
    publish_date=models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to='gallery/',default='1.0')

class Testimonials(models.Model):
    full_name=models.CharField(max_length=100,default='')
    designation=models.CharField(max_length=100,default='')
    testimonial=models.TextField(max_length=250,default='')
    publish=models.BooleanField(default=True)
    publish_date=models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to='testimonial/',default='https://mdbootstrap.com/img/Photos/Avatars/img%20(30).jpg')

class Companies(models.Model):
    publish=models.BooleanField(default=True)
    publish_date=models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to='company/',default='https://via.placeholder.com/150C')

# Event management page

# Our events page

# Contact us page
