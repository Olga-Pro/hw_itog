from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flowers/', views.flower_list, name='flower_list'),
   ]
