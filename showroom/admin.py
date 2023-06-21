from django.contrib import admin
from .models import Showroom
# Register your models here.

class CustomShowroomAdmin(admin.ModelAdmin):
    pass

admin.site.register(Showroom, CustomShowroomAdmin)