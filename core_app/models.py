from django.db import models


class Laptops(models.Model):
    """ Класс ноутбук """

    url = models.CharField(max_length=255, unique=True, verbose_name='Ссылка')
    title = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    manufacturer = models.CharField(max_length=200)
    screen_diagonal = models.CharField(max_length=30)
    screen_resolution = models.CharField(max_length=30)
    operating_system = models.CharField(max_length=50)
    processor = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    video_card_type = models.CharField(max_length=50)
    video_card = models.CharField(max_length=100)
    storage_type = models.CharField(max_length=50)
    storage_capacity = models.CharField(max_length=100)
    battery_life = models.CharField(max_length=20)
    status = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'

    def __str__(self):
        return f'{self.title} | {self.price}'


class Image(models.Model):
    """ Изображения """

    image = models.URLField(max_length=255, unique=True)
    laptop = models.ForeignKey(Laptops, on_delete=models.CASCADE, related_name='image')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.image


