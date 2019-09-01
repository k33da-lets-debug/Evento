from django.contrib import admin
from .models import CreateEvent,Carosoul,Gallery,Testimonials,Companies,ContactUs

# Admin class definations
class CreateEventAdmin(admin.ModelAdmin):
    fields=['first_name','last_name','email','contact_no','category','company_name','date','event_description']
    list_filter = ('date','category')
    list_display = ('first_name','last_name','email','contact_no','category','company_name','date','event_description')

    class Meta:
        verbose_name = 'Create event query'
        verbose_name_plural = 'Create event queries'

class CarouselAdmin(admin.ModelAdmin):
    fields=['title','subtitle','short_description','publish','publish_date','image']
    list_filter = ('publish_date',)
    list_display = ('title','subtitle','short_description','publish','publish_date','image')

    class Meta:
        verbose_name = 'Carousel detail'
        verbose_name_plural = 'Carousel details'

class GalleryAdmin(admin.ModelAdmin):
    fields=['publish','publish_date','image']
    list_filter = ('publish_date',)
    list_display = ('publish','publish_date','image')

    class Meta:
        verbose_name = 'Gallery detail'
        verbose_name_plural = 'Gallery details'

class TestimonialAdmin(admin.ModelAdmin):
    fields=['full_name','designation','testimonial','publish','publish_date','image']
    list_filter = ('publish_date',)
    list_display = ('full_name','designation','testimonial','publish','publish_date','image')

    class Meta:
        verbose_name = 'Testimonial detail'
        verbose_name_plural = 'Testimonial details'

class CompanyAdmin(admin.ModelAdmin):
    fields=['publish','publish_date','image']
    list_filter = ('publish_date',)
    list_display = ('publish','publish_date','image')

    class Meta:
        verbose_name = 'Company detail'
        verbose_name_plural = 'Companies details'

class ContactUsAdmin(admin.ModelAdmin):
    fields=['first_name','last_name','email','contact_no','message']
    list_display = ('first_name','last_name','email','contact_no','message')

    class Meta:
        verbose_name = 'Create event query'
        verbose_name_plural = 'Create event queries'


# Admin class registrations
admin.site.register(CreateEvent, CreateEventAdmin)

admin.site.register(Carosoul, CarouselAdmin)

admin.site.register(Gallery, GalleryAdmin)

admin.site.register(Testimonials, TestimonialAdmin)

admin.site.register(Companies, CompanyAdmin)

admin.site.register(ContactUs, ContactUsAdmin)