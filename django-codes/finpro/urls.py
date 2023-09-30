from django.urls import path
from . import views

urlpatterns = [
    path('post_new/', views.post_new, name='post_new'),
    path('text/<int:pk>/', views.text_detail, name='text_detail'),
    path('text/', views.text_list, name='text_list'),
]