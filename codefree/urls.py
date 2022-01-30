from django.urls import path
from . import views

urlpatterns = [
    path('accounts/profile/', views.profile,name="profile"),
    path('add/', views.add, name="add"),
    path('', views.profile, name="profile2"),
]