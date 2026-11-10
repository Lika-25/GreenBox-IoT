from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва датчика")
    sensor_type = models.CharField(max_length=50, verbose_name="Тип (Температура, Вологість тощо)")
    pin = models.CharField(max_length=20, verbose_name="Пін підключення", blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Активний")

    def __str__(self):
        return f"{self.name} ({self.sensor_type})"