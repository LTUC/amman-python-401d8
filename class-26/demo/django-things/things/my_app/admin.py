from django.contrib import admin
from .models import Thing, CoolThing


@admin.register(Thing)
class AdminThing(admin.ModelAdmin):
    pass


@admin.register(CoolThing)
class AdminCoolThing(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_cool']