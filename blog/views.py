from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post, Category
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    return render_to_response('blog/index.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.order_by('-posted_date')[:5]
    })

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    categories = post.categories.all()
    return render_to_response('blog/view_post.html', {
        'post': post,
        'categories':categories
    })

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('blog/view_category.html', {
        'category': category,
        'posts': Post.objects.filter(categories=category)[:5]
    })