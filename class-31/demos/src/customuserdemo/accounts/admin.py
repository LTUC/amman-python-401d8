from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "phone_number"]

    fieldsets =  UserAdmin.fieldsets + (
        ("contact number", {"fields": ("phone_number",)}),
    )
    # fieldsets = UserAdmin.fieldsets + (
    #     ("contact number", {"fields": ("phone_number", )})
    # )



