# Настройки администратора системы

from django.contrib import admin
from .models import Slot_1, Slot_2, Slot_3, Slot_4, Slot_5, Slot_6


# Register your models here.
class Slot1Admin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('device_model', {'fields': ['device_model']}),
        ('charge', {'fields': ['charge']}),
        ('connection_time', {'fields': ['connection_time']}),
        ('disconnection_time', {'fields': ['disconnection_time']}),
        ('date', {'fields': ['date']})
    ]


class Slot2Admin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('device_model', {'fields': ['device_model']}),
        ('charge', {'fields': ['charge']}),
        ('connection_time', {'fields': ['connection_time']}),
        ('disconnection_time', {'fields': ['disconnection_time']}),
        ('date', {'fields': ['date']})
    ]


class Slot3Admin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('device_model', {'fields': ['device_model']}),
        ('charge', {'fields': ['charge']}),
        ('connection_time', {'fields': ['connection_time']}),
        ('disconnection_time', {'fields': ['disconnection_time']}),
        ('date', {'fields': ['date']})
    ]


class Slot4Admin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('device_model', {'fields': ['device_model']}),
        ('charge', {'fields': ['charge']}),
        ('connection_time', {'fields': ['connection_time']}),
        ('disconnection_time', {'fields': ['disconnection_time']}),
        ('date', {'fields': ['date']})
    ]


class Slot5Admin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('device_model', {'fields': ['device_model']}),
        ('charge', {'fields': ['charge']}),
        ('connection_time', {'fields': ['connection_time']}),
        ('disconnection_time', {'fields': ['disconnection_time']}),
        ('date', {'fields': ['date']})
    ]


class Slot6Admin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('device_model', {'fields': ['device_model']}),
        ('charge', {'fields': ['charge']}),
        ('connection_time', {'fields': ['connection_time']}),
        ('disconnection_time', {'fields': ['disconnection_time']}),
        ('date', {'fields': ['date']})
    ]


admin.site.register(Slot_1, Slot1Admin)
admin.site.register(Slot_2, Slot2Admin)
admin.site.register(Slot_3, Slot3Admin)
admin.site.register(Slot_4, Slot4Admin)
admin.site.register(Slot_5, Slot5Admin)
admin.site.register(Slot_6, Slot6Admin)
