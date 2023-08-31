from django.contrib import admin
from .models import Part, SubPart, Introduction, AboutUs, ContactInfo, PythonCode

# Register your models here.
admin.site.register(Part)
admin.site.register(SubPart)
admin.site.register(Introduction)
admin.site.register(AboutUs)
admin.site.register(ContactInfo)
admin.site.register(PythonCode)
