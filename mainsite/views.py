from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from mainsite.models import *

def index(request):
    #get about me post
    about_me = SpecialSection.objects.filter(is_published=True).filter(section_name="about_me").order_by('-published_date')[0]
    #get thought of the day
    thought_of_the_day = SpecialSection.objects.filter(is_published=True).filter(section_name="thought_of_the_day").order_by('-published_date')[0]

    return render_to_response('mainsite/index.html', {
        'about_me': about_me,
        'thought_of_the_day':thought_of_the_day
    })

