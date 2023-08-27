from django.contrib import admin
from .models import Content, Introduction, AboutUs, ContactInfo

# Register your models here.
admin.site.register(Content)
admin.site.register(Introduction)
admin.site.register(AboutUs)
admin.site.register(ContactInfo)
