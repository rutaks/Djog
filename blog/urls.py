from django.urls import path
from . import views

"""
BLOG ROUTES
"""

urlpatterns = [
    path('', views.home, name="blog-home"),
]
