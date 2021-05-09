from django.db import models


class Transport(models.Model):
    type = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Line(models.Model):
    transport = models.OneToOneField(Transport, on_delete=models.CASCADE, primary_key=True)
    initial_node = models.CharField(max_length=100)
    final_node = models.CharField(max_length=100)


class Timetable(models.Model):
    transport = models.OneToOneField(Transport, on_delete=models.CASCADE, primary_key=True)
    departure_time = models.TimeField()


class Vehicle(models.Model):
    CHOICES = (
        ('taxi', 'Taxi'),
        ('car', 'Car'),
        ('on foot', 'On foot'),
        ('bike', 'Bike'),
    )
    vehicle = models.CharField(choices=CHOICES, max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
