from .models import *
# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('phone_number',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'phone_number', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'phone_number')
    list_display = ('username', 'phone_number', 'is_staff')
    ordering = ('username',)


class CustomProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "first_name", "last_name", "email"]


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, CustomProfileAdmin)
