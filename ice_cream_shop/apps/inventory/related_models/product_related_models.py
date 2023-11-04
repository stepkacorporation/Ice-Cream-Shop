from django.db import models


class ProductBrand(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название бренда')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд продукта'
        verbose_name_plural = 'Бренды продукта'
        ordering = ('name', )


class ProductType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название вида')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид продукта'
        verbose_name_plural = 'Виды продукта'
        ordering = ('name', )


class ProductSupplements(models.Model):
    name = models.TextField(verbose_name='Добавки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Добавки продукта'
        verbose_name_plural = 'Добавки продукта'
        ordering = ('name', )


class ProductTypeOfPackaging(models.Model):
    name = models.CharField(max_length=255, verbose_name='Вид упаковки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид упаковки'
        verbose_name_plural = 'Виды упаковки'
        ordering = ('name', )


class ProductFeatures(models.Model):
    name = models.CharField(max_length=255, verbose_name='Особенности продукта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Особенности продукта'
        verbose_name_plural = 'Особенности продукта'
        ordering = ('name', )


class ProductStandard(models.Model):
    name = models.CharField(max_length=255, verbose_name='Стандарт продукта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Стандарт продукта'
        verbose_name_plural = 'Стандарты продукта'
        ordering = ('name',)


class ProductTaste(models.Model):
    name = models.CharField(max_length=255, verbose_name='Вкус продукта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вкус продукта'
        verbose_name_plural = 'Вкусы продукта'
        ordering = ('name',)


class ProductProducingCountry(models.Model):
    name = models.CharField(max_length=255, verbose_name='Страна-производитель продукта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна-производитель продукта'
        verbose_name_plural = 'Страны-производители продукта'
        ordering = ('name',)


class ProductManufacturer(models.Model):
    name = models.CharField(max_length=255, verbose_name='Производитель продукта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель продукта'
        verbose_name_plural = 'Производители продукта'
        ordering = ('name',)