from readings.views import BookViewSet
from rest_framework import routers
from django.urls import path

urlpatterns = [
    path('books/',
         BookViewSet.as_view({'get': 'list', 'post': 'create'}), name='books'),
    path('books/<int:pk>/', BookViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='book'),
]