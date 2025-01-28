from email.policy import default
from tabnanny import verbose

from django.db import models

class Book(models.Model):
    GENDER_CHOICES = (
        ('Ужасы', 'Ужасы'),
        ('Комедия', 'Комедия'),
        ('Романтика', 'Романтика'),
    )
    image = models.ImageField(upload_to='books/', verbose_name='Изображение', null=True, blank=True)
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    genre = models.CharField(choices=GENDER_CHOICES, max_length=20, verbose_name='Жанр')
    email = models.EmailField(verbose_name='Почта')
    author = models.CharField(max_length=50, verbose_name='Автор')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Книга'
        verbose_name_plural='Книги'

class Review(models.Model):
    STARS =(
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
    )
    comment = models.TextField(verbose_name='Коментарий')
    stars = models.CharField(choices=STARS, max_length=10, verbose_name='Оценка', default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.book.title

    class Meta:
        verbose_name='Коментарий'
        verbose_name_plural='Коментарии'
