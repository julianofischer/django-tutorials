from django.contrib import admin

# Register your models here.
from .models import MonitoredItem

admin.site.register(MonitoredItem)
