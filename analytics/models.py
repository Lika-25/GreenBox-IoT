from django.db import models

class AnalyticsReport(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва звіту")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата генерації")
    average_temperature = models.FloatField(verbose_name="Середня температура (°C)", default=0.0)
    average_humidity = models.FloatField(verbose_name="Середня вологість (%)", default=0.0)
    avg_soil_moisture = models.FloatField(verbose_name="Середня вологість ґрунту (%)", default=0.0)
    avg_light_level = models.FloatField(verbose_name="Середня освітлення (lux)", default=0.0)
    notes = models.TextField(blank=True, null=True, verbose_name="Примітки")

    STATUS_CHOICES = [
        ('good', '🌿 Здоровий стан'),
        ('warning', '⚠️ Потребує уваги'),
        ('danger', '🚨 Критично'),
    ]
    plant_health_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='good',
        verbose_name="Статус фітобокса"
    )

    def __str__(self):
        return f"{self.title} від {self.created_at.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Аналітичний звіт"
        verbose_name_plural = "Аналітичні звіти"
