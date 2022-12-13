# Структура базы данных проекта

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Slot_1(models.Model):
    name = models.CharField(max_length=100)
    device_model = models.CharField(max_length=100)
    charge = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    connection_time = models.CharField(max_length=5)
    disconnection_time = models.CharField(max_length=5)
    date = models.DateField()


class Slot_2(models.Model):
    name = models.CharField(max_length=100)
    device_model = models.CharField(max_length=100)
    charge = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    connection_time = models.CharField(max_length=5)
    disconnection_time = models.CharField(max_length=5)
    date = models.DateField()


class Slot_3(models.Model):
    name = models.CharField(max_length=100)
    device_model = models.CharField(max_length=100)
    charge = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    connection_time = models.CharField(max_length=5)
    disconnection_time = models.CharField(max_length=5)
    date = models.DateField()


class Slot_4(models.Model):
    name = models.CharField(max_length=100)
    device_model = models.CharField(max_length=100)
    charge = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    connection_time = models.CharField(max_length=5)
    disconnection_time = models.CharField(max_length=5)
    date = models.DateField()


class Slot_5(models.Model):
    name = models.CharField(max_length=100)
    device_model = models.CharField(max_length=100)
    charge = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    connection_time = models.CharField(max_length=5)
    disconnection_time = models.CharField(max_length=5)
    date = models.DateField()


class Slot_6(models.Model):
    name = models.CharField(max_length=100)
    device_model = models.CharField(max_length=100)
    charge = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    connection_time = models.CharField(max_length=5)
    disconnection_time = models.CharField(max_length=5)
    date = models.DateField()

