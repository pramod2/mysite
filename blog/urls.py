from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(
        r'^view/(?P<slug>[^\.]+).html',
        views.post,
        name='view_blog_post'),
    url(
        r'^category/(?P<slug>[^\.]+).html',
        views.category,
        name='view_blog_category'),
]
