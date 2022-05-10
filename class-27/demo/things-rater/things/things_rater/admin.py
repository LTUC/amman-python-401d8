import imp
from django.contrib import admin
from .models import Thing

@admin.register(Thing)
class AdminThing(admin.ModelAdmin):
    list_display = ['id','name', 'rating', 'reviewer']
    search_fields = ('name', )


# admin.site.register(Thing)