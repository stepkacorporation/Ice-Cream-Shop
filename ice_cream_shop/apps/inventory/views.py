from django.shortcuts import render
from django.views.generic import ListView

from .models import Product


class CatalogView(ListView):
    model = Product
    template_name = 'inventory/catalog.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = 'Каталог'
        context['current_url'] = self.request.path
        return context

    def get_queryset(self):
        return Product.objects.all()

# def catalog(request):
#     return render(request, 'inventory/catalog.html')
