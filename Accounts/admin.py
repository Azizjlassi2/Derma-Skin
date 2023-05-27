from django.contrib import admin
from .models import AppUser
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ("username","email","user_type","age","gouvernorat","city","created")

admin.site.register(AppUser,UserAdmin)