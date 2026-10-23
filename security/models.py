from django.db import models

class SecurityMeasure(models.Model):
    CATEGORY_CHOICES = [
        ('Кібербезпека', 'Кібербезпека (Мережа та дані)'),
        ('Фізична безпека', 'Фізична безпека (Обладнання)'),
        ('Охорона праці', 'Охорона праці (Персонал)'),
    ]

    title = models.CharField(max_length=150, verbose_name="Назва заходу / засобу")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Кібербезпека', verbose_name="Категорія")
    description = models.TextField(verbose_name="Опис та правила застосування")
    responsible = models.CharField(max_length=100, default="Адміністратор безпеки", verbose_name="Відповідальна особа")
    is_active = models.BooleanField(default=True, verbose_name="Статус (Впроваджено)")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Останнє оновлення")

    def __str__(self):
        return f"{self.title} ({self.category})"