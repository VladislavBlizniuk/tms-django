from django.shortcuts import render, get_object_or_404

from .models import Category, Product
# Create your views here.
def index(request):
    return render(request,'shop/index.html', {
        'categories': Category.objects.all(),
    })


def category_detail(request,category_id: int):
    return render(request, 'shop/category_detail.html', {
        'category': get_object_or_404(Category, id=category_id),
    })