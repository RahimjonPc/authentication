from django.urls import path, include
from .views import index, restricted

urlpatterns = [
    path('checkserver/', index, name='index'),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('restricted/', restricted),
]
