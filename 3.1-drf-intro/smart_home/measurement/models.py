from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(decimal_places=2, max_digits=5)
    measurement_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sensor_id.name} - {self.temperature}°C измерено {self.measurement_time}"