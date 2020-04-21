from django.urls import path
from . import views

"""
BLOG ROUTES
"""

urlpatterns = [
    path('register', views.register, name="user-register"),
]
