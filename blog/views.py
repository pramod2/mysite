from blog.models import Post, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def index(request):
    return render_to_response('blog/index.html', {}, context_instance=RequestContext(request))

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    categories = post.categories.all()
    return render_to_response('blog/view_post.html', {
        'post': post,
        'categories':categories
    }, context_instance=RequestContext(request))

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('blog/view_category.html', {
        'category': category,
        'posts': Post.objects.filter(categories=category)[:5]
    }, context_instance=RequestContext(request))