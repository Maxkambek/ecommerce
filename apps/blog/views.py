from django.shortcuts import render
from .models import Post, Tag
from ..products.models import Category


def blog_list(request):
    blogs = Post.objects.order_by('-id')
    categories = Category.objects.order_by('-id')
    tags = Tag.objects.all()
    tag=request.GET.get('tag')
    cat=request.GET.get('cat')
    search=request.GET.get('search')
    if cat:
        blogs=blogs.filter(category__title__exact=cat)
    if tag:
        blogs=blogs.filter(tags__title__iexact=tag)
    if search:
        blogs=blogs.filter(title__icontains=search)
    ctx = {
        'blogs': blogs,
        'categories': categories,
        'tags': tags,
    }

    return render(request, 'blog.html', ctx)


def blog_detail(request, pk):
    blogs = Post.objects.order_by('-id')
    blog = Post.objects.get(id=pk)
    categories = Category.objects.order_by('-id')
    tags = Tag.objects.all()

    ctx = {
        'blog': blog,
        'blogs': blogs,
        'categories': categories,
        'tags': tags,
    }

    return render(request, 'blog-details.html', ctx)
