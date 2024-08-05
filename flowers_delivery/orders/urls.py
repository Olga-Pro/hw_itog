from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:flower_id>/', views.create_order, name='create_order'),
]
