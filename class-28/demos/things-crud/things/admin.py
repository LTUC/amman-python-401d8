from django.contrib import admin
from .models import Thing


@admin.register(Thing)
class AdminThing(admin.ModelAdmin):
    list_display = ["name", "reviewer","rating"]

