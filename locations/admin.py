from django.contrib import admin

# Register your models here.
from .models import Service
from .models import TestQuestion

admin.site.register(Service)
admin.site.register(TestQuestion)