from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название рецепта")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    UNITS = [
        ('g', 'граммы'),
        ('kg', 'килограммы'),
        ('ml', 'миллилитры'),
        ('l', 'литры'),
        ('pcs', 'штуки'),
    ]

    name = models.CharField(max_length=100, verbose_name="Название ингредиента")
    quantity = models.FloatField(verbose_name="Количество")
    unit = models.CharField(max_length=10, choices=UNITS, verbose_name="Единица измерения")
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.quantity} {self.get_unit_display()}"
