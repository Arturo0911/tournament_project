from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('api/', views._index_post, name="api"),
]