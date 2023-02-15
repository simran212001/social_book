from django.contrib import admin
from .models import CustomUser,Book
# Register your models here.
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser)
admin.site.register(Book)