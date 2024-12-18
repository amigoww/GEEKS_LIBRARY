from django.db import models

class BookModel(models.Model):
    GENRE = (
        ('Фентези', 'Фентези'),
        ('Комедия', 'Комедия'),
        ('Детектив', 'Детектив')
    )
    image = models.ImageField(upload_to='books/', verbose_name='Загрузите фото Книги')
    title = models.CharField(max_length=100, verbose_name='Укажите название книги')
    description = models.TextField(verbose_name='Укажите описание', blank=True)
    price = models.FloatField(verbose_name='Задайте цену книги', default=25)
    created_at = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=100, choices=GENRE, default='Детектив')
    gmail = models.EmailField(verbose_name='Укажите эл.почту автора', null=True)
    author = models.CharField(max_length=100, verbose_name='Укажите автора', default='Азамат Айталиев')
    audio_book = models.URLField(verbose_name='Укажите ссылку аудио книги')


    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title