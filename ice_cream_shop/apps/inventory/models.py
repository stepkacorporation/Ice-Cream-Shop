from django.db import models
from django.urls import reverse

from .related_models.product_related_models import ProductBrand, ProductType, ProductSupplements,\
    ProductTypeOfPackaging, ProductFeatures, ProductStandard, ProductTaste, ProductProducingCountry, \
    ProductManufacturer


class Product(models.Model):
    # Основное
    name = models.CharField(max_length=255, verbose_name='Название товара')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    price = models.PositiveIntegerField(verbose_name='Цена')
    image = models.ImageField(verbose_name='Изображение')

    # Заводские данные о товаре
    brand = models.ForeignKey(ProductBrand, on_delete=models.PROTECT, verbose_name='Бренд')
    code = models.PositiveIntegerField(verbose_name='Код товара')

    # Основные характеристики
    type = models.ForeignKey(ProductType, on_delete=models.PROTECT, verbose_name='Вид мороженного')
    supplements = models.ForeignKey(ProductSupplements, on_delete=models.PROTECT, verbose_name='Добавки')
    on_a_stick = models.BooleanField(default=False, verbose_name='На палочке')
    type_of_packaging = models.ForeignKey(ProductTypeOfPackaging, on_delete=models.PROTECT, verbose_name='Вид упаковки')
    features = models.ForeignKey(ProductFeatures, on_delete=models.PROTECT, verbose_name='Особенности')
    standard = models.ForeignKey(ProductStandard, on_delete=models.PROTECT, verbose_name='Стандарт')
    weight_in_grams = models.PositiveIntegerField(verbose_name='Вес, в граммах')
    taste = models.ForeignKey(ProductTaste, on_delete=models.PROTECT, verbose_name='Вкус')
    in_the_glaze = models.BooleanField(default=False, verbose_name='В глазури')
    producing_country = models.ForeignKey(
        ProductProducingCountry, on_delete=models.PROTECT, verbose_name='Страна-производитель'
    )
    manufacturer = models.ForeignKey(ProductManufacturer, on_delete=models.PROTECT, verbose_name='Производитель')

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
        return f'{self.name}, {self.manufacturer}, {self.type_of_packaging}, {self.weight_in_grams} г.'

    def get_absolute_url(self):
        return reverse('product_info', kwargs={'product_slug': self.slug})

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


