from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'schedule')
    search_fields = ('name',)
    list_editable = ('schedule',)


# admin.site.register(models.Movie, MovieAdmin)
