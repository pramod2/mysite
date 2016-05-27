from blog.models import Post, Category

def posts_and_categories_processor(request):
    return {'all_categories': Category.objects.all(),'recent_posts': Post.objects.filter(is_published=True).order_by('-published_date')[:5]}

