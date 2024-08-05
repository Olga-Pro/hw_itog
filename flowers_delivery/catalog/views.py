from django.shortcuts import render
from .models import Flower

from django.views.generic import ListView, DetailView


class ProductListView(ListView):
    model = Flower
    template_name = 'catalog/flower_list.html'


class ProductDetailView(DetailView):
    model = Flower
    template_name = 'catalog/product_detail.html'


def flower_list(request):
    flowers = Flower.objects.all()

    return render(request, 'catalog/flower_list.html', {'flowers': flowers})


def home(request):
    return render(request, 'catalog/home.html')