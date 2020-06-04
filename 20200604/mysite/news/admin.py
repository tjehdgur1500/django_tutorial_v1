from django.contrib import admin
from . import models

# Register your models here.
class ReporterAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Article)
admin.site.register(models.Reporter)
