from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_profile, name= "profile_page"),
    path('post_profile/', views.post_profile, name = "post_profile_pages"),
    path('update/<int:id>/', views.update_profile, name= "update"),
    path('delete/<int:id>/', views.delete_profile,name= "delete_profile"),
]