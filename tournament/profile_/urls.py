from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_profile, name= "profile_page"),
    path('post_profile/', views.post_profile, name = "post_profile_pages"),
    path('update/', views.update_profile, name= "update"),
]