from django.db import models

class GreenhouseInfo(models.Model):
    name = models.CharField(max_length=100, default="Фітобокс №1", verbose_name="Назва теплички")
    area = models.FloatField(help_text="Введіть площу в квадратних метрах", verbose_name="Площа (кв. м)")
    volume = models.FloatField(help_text="Введіть об'єм у літрах", verbose_name="Об'єм (л)")
    height = models.FloatField(help_text="Введіть висоту в метрах", verbose_name="Висота (м)")
    description = models.TextField(blank=True, null=True, verbose_name="Додатковий опис або статус")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Час останнього оновлення")

    def __str__(self):
        return f"{self.name} (Площа: {self.area} м², Об'єм: {self.volume} л)"