from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'author': 'Rutakayile Samuel',
        'title': 'How good is Django',
        'content': 'Django is a really good Framework for python',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Rutakayile Samuel',
        'title': 'How good is Django',
        'content': 'Django is a really good Framework for python',
        'date_posted': 'August 27, 2018'
    }
]

"""
BLOG VIEWS
"""


def home(request):
    context = {
        'title': 'Home',
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)
