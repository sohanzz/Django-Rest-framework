import django

from django.contrib import admin
from .models import Drink

@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
	list_display = ('name',)
