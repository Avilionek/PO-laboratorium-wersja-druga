
from django.urls import path
from .import views

app_name = 'Shop'
urlpatterns = [
    path('', views.pc, name='pc'),
    path('harddrive/', views.harddrive, name='harddrive'),
    path('design/', views.design, name='design'),
    path('graphicscard/', views.graphicscard, name='graphicscard'),
    path('pcform/', views.pcform, name='pcform')
]
