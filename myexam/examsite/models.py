from django.db import models
from django.contrib.auth.models import User  
from django.utils import timezone 

class akexam(models.Model):
    exam_name = models.CharField(max_length=100, verbose_name="Название экзамена")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    exam_date = models.DateField(verbose_name="Дата проведения экзамена")

    exam_image = models.ImageField(
        upload_to="exam_images/", 
        verbose_name="Изображение задания",
        blank=True,  # Необязательное поле
        null=True    # Может быть пустым в БД
    )

    assigned_users = models.ManyToManyField(
        User, 
        verbose_name="Назначенные пользователи",
        related_name="assigned_exams"  # Для обратного доступа
    )

    is_public = models.BooleanField(default=False, verbose_name="Опубликовано")

    def __str__(self):
        return f"{self.exam_name} (Дата: {self.exam_date})"

    class Meta:
        verbose_name = "Экзамен"
        verbose_name_plural = "Экзамены"
