from django.contrib import admin
from .models import Documento

# Register your models here.
class DocAdmin(admin.ModelAdmin):
    readonly_fields=('thumb',)

admin.site.register(Documento, DocAdmin)
