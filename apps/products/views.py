from django.shortcuts import render
from .models import Product, Category, ProductImage
from apps.blog.models import Post


def index(request):
    products = Product.objects.all().order_by('-id')
    categories = Category.objects.all()
    latest_products = products[:6]
    top_rated_products = products.order_by('-mid_rate')[:6]
    top_viewed_products = products.order_by('-views')[:6]
    blog_latest = Post.objects.order_by('-id')[:3]
    cat = request.GET.get('cat')
    search = request.GET.get('search')
    if cat:
        products=products.filter(category__title__exact=cat)
    if search:
        products=products.filter(name__icontains=search)

    ctx = {
        'products': products,
        'categories': categories,

        'latest_products': latest_products,
        'top_rated_products': top_rated_products,
        'top_viewed_products': top_viewed_products,
        'blog_latest': blog_latest
    }

    return render(request, 'index.html', ctx)


def shop_grid(request):
    products = Product.objects.all().order_by('-id')
    categories = Category.objects.all()
    latest_products = products[:6]
    sale_ofs=products[:6]
    cat = request.GET.get('cat')
    search = request.GET.get('search')
    if cat:
        products = products.filter(category__title__exact=cat)
    if search:
        products = products.filter(name__icontains=search)

    ctx = {
        'products': products,
        'categories': categories,
        'latest_products': latest_products,
        'sale_ofs':sale_ofs,

    }

    return render(request, 'shop-grid.html', ctx)


def shop_detail(request,pk):
    product=Product.objects.get(id=pk)
    products=Product.objects.all().order_by('-id')[:4]
    categories=Category.objects.all()
    images=product.productimage_set.all()
    ctx={
        'product':product,
        'categories':categories,
        'images':images,
        'products':products,
    }

    return render(request,'shop-details.html',ctx)



