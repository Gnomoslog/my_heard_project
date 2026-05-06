from django.db import models

class Post(models.Model):
    """Модель поста для социальной сети Yatube"""
    text = models.TextField(
        verbose_name='Текст поста',
        help_text='Введите текст вашего поста'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    slug = models.SlugField(
        max_length=200,
        unique=False,
        verbose_name='Слаг группы',
        blank=True,
        null=True,
        help_text='Короткое имя группы (например: python, django)'
    )
    
    def __str__(self):
        return self.text[:50]
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-pub_date']