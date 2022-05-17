from django.contrib import admin
from .models import Item, Meal


@admin.register(Item)
class AdminItem(admin.ModelAdmin):
    list_display = ['name', 'price']


@admin.register(Meal)
class AdminMeal(admin.ModelAdmin):
    list_display = ['name', 'id']