from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    body = models.CharField(max_length=150, verbose_name='Содержимое')
    slug = models.CharField(max_length=150, verbose_name='slug')
    preview = models.ImageField(upload_to='blog_media/', verbose_name='Превью блога', **NULLABLE)
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        # Строковое отображение объекта
        return {self.title}

    class Meta:
        verbose_name = 'Блог'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Блоги'  # Настройка для наименования набора объектов
