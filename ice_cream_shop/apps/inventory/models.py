from django.db import models


class Product(models.Model):
    # Основное
    name = models.CharField(max_length=255, verbose_name='Название товара')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    price = models.PositiveIntegerField(verbose_name='Цена')

    # Заводские данные о товаре
    brand = models.CharField(max_length=255, verbose_name='Бренд')
    code = models.PositiveIntegerField(verbose_name='Код товара')

    # Основные характеристики
    type = models.CharField(max_length=255, verbose_name='Вид мороженного')
    supplements = models.CharField(max_length=255, verbose_name='Добавки')
    on_a_stick = models.BooleanField(default=False, verbose_name='На палочке')
    type_of_packaging = models.CharField(max_length=255, verbose_name='Вид упаковки')
    features = models.CharField(max_length=255, verbose_name='Особенности')
    standard = models.CharField(max_length=255, verbose_name='Стандарт')
    weight_in_grams = models.PositiveIntegerField(verbose_name='Вес, в граммах')
    taste = models.CharField(max_length=255, verbose_name='Вкус')
    in_the_glaze = models.BooleanField(default=False, verbose_name='В глазури')
    producing_country = models.CharField(max_length=255, verbose_name='Страна-производитель')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель')

    # Пищевая ценность
    energy_value = models.PositiveIntegerField(verbose_name='Энергетическая ценность (ккал на 100 г)')
    fats_in_grams = models.PositiveIntegerField(verbose_name='Жиры, в граммах (на 100 г)')
    proteins_in_grams = models.PositiveIntegerField(verbose_name='Белки, в граммах (на 100 г)')
    carbohydrates_in_grams = models.PositiveIntegerField(verbose_name='Углеводы, в граммах (на 100 г)')

    # Хранение
    storage_temperature = models.CharField(max_length=255, verbose_name='Температура хранения')
    expiration_date = models.CharField(max_length=255, verbose_name='Срок годности')

    # Кол-во
    quantity = models.PositiveIntegerField(verbose_name='Кол-во')

    def __str__(self):
        return f'{self.name} {self.manufacturer} {self.weight_in_grams}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('id', )


class Supplier(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название поставщика')
    address = models.CharField(max_length=255, verbose_name='Адрес поставщика')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Эл. почта')
    website = models.URLField(max_length=255, blank=True, null=True, verbose_name='Веб-сайт поставщика')
    additional_notes = models.TextField(blank=True, null=True, verbose_name='Дополнительные заметки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ('id', )


class StockEntry(models.Model):
    product = models.ForeignKey('Product', on_delete=models.PROTECT, verbose_name='Товар')
    delivery_date = models.DateField(auto_now_add=True, verbose_name='Дата поставки')
    quantity_delivered = models.PositiveIntegerField(verbose_name='Кол-во поставленных товаров')
    purchase_price = models.PositiveIntegerField(verbose_name='Цена закупки')
    supplier = models.ForeignKey('Supplier', on_delete=models.PROTECT, verbose_name='Поставщик')
    notes = models.TextField(blank=True, null=True, verbose_name='Заметки о поставке')

    def __str__(self):
        return f'{self.product} {self.delivery_date}'

    class Meta:
        verbose_name = 'Поставка товара'
        verbose_name_plural = 'Поставки товаров'
        ordering = ('-id', '-delivery_date')
