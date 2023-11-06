from django.db import models
from django.db.models import Q
from django.views.generic import ListView, DetailView

from .models import Product
from .forms import ProductFilterForm
from .related_models.product_related_models import ProductBrand, ProductType, ProductManufacturer, ProductTaste


class ProductListView(ListView):
    model = Product
    template_name = 'inventory/catalog.html'
    context_object_name = 'products'
    form_class = ProductFilterForm
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = 'Каталог'
        context['current_url'] = self.request.path

        # Передаем фильтры в контекст
        max_price = Product.objects.aggregate(max_price=models.Max('price'))['max_price']
        context['max_price'] = max_price or 1
        max_weight = Product.objects.aggregate(weight_in_grams=models.Max('weight_in_grams'))['weight_in_grams']
        context['max_weight'] = max_weight or 1
        context['product_brands'] = ProductBrand.objects.all()
        context['product_types'] = ProductType.objects.all()
        context['product_manufacturers'] = ProductManufacturer.objects.all()
        context['product_tastes'] = ProductTaste.objects.all()

        # Получаем значения фильтров из GET-параметров и сохраняем их в контексте
        selected_min_price = self.request.GET.get('min_price')
        selected_max_price = self.request.GET.get('max_price', max_price)
        selected_brands = self.request.GET.getlist('brands')
        selected_types = self.request.GET.getlist('types')
        selected_min_weight = self.request.GET.get('min_weight')
        selected_max_weight = self.request.GET.get('max_weight', max_weight)
        selected_manufacturers = self.request.GET.getlist('manufacturers')
        selected_tastes = self.request.GET.getlist('tastes')

        context['selected_min_price'] = selected_min_price
        context['selected_max_price'] = selected_max_price
        context['selected_brands'] = selected_brands
        context['selected_types'] = selected_types
        context['selected_min_weight'] = selected_min_weight
        context['selected_max_weight'] = selected_max_weight
        context['selected_manufacturers'] = selected_manufacturers
        context['selected_tastes'] = selected_tastes

        # Получаем результаты поиска и передаем их в контекст
        search_query = self.request.GET.get('query', '')
        context['search_query'] = search_query
        if search_query:
            context['products'] = Product.objects.filter(name__icontains=search_query)

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.form_class(self.request.GET)
        if form.is_valid():
            filters = Q()

            min_price = form.cleaned_data['min_price']
            max_price = form.cleaned_data['max_price']
            brands = form.cleaned_data['brands']
            types = form.cleaned_data['types']
            min_weight = form.cleaned_data['min_weight']
            max_weight = form.cleaned_data['max_weight']
            tastes = form.cleaned_data['tastes']
            manufacturers = form.cleaned_data['manufacturers']

            if min_price:
                filters &= Q(price__gte=min_price)
            if (max_price, 1)[max_price == 0]:
                filters &= Q(price__lte=max_price)
            if brands:
                filters &= Q(brand__in=brands)
            if types:
                filters &= Q(type__in=types)
            if min_weight:
                filters &= Q(weight_in_grams__gte=min_weight)
            if (max_weight, 1)[max_weight == 0]:
                filters &= Q(weight_in_grams__lte=max_weight)
            if tastes:
                filters &= Q(taste__in=tastes)
            if manufacturers:
                filters &= Q(manufacturer__in=manufacturers)

            search_query = self.request.GET.get('query')
            if search_query:
                filters &= Q(name__icontains=search_query)

            queryset = queryset.filter(filters)

        return queryset


class ShowProductInfo(DetailView):
    model = Product
    template_name = 'inventory/product_info.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['product']
        return context
