
from django.urls import path
from .import views


urlpatterns = [
    path('', views.pc, name='pc'),
    path('harddrive/', views.harddrive, name='harddrive'),
    path('design/', views.design, name='design'),
    path('graphicscard/', views.graphicscard, name='graphicscard'),
]
