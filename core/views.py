from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product, Service, GalleryPhoto
from .forms import BookingForm


def home(request):
    featured_products = Product.objects.filter(is_featured=True, is_available=True)[:9]
    all_products = Product.objects.filter(is_available=True)
    services = Service.objects.filter(is_featured=True).order_by('order')
    return render(request, 'core/home.html', {
        'products': featured_products,
        'all_products': all_products,
        'services': services,
    })


def showroom(request):
    category = request.GET.get('category', '')
    products = Product.objects.filter(is_available=True)
    if category:
        products = products.filter(category=category)
    return render(request, 'core/showroom.html', {
        'products': products,
        'active_category': category,
        'categories': Product.CATEGORY_CHOICES,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)
    related = Product.objects.filter(
        category=product.category, is_available=True
    ).exclude(pk=product.pk)[:4]
    return render(request, 'core/product_detail.html', {
        'product': product,
        'related': related,
    })


def about(request):
    gallery = GalleryPhoto.objects.filter(is_active=True)[:9]
    return render(request, 'core/about.html', {'gallery': gallery})


def contact(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request has been sent! Thelma will contact you soon.')
            return redirect('contact')
    else:
        form = BookingForm()
    return render(request, 'core/contact.html', {'form': form})
