from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.cv_create, name='cv_create'),
    path('list/', views.cv_list, name='cv_list'),
    path('view/<int:pk>/', views.cv_detail, name='cv_detail'),
    path('download/<int:pk>/', views.download_cv, name='download_cv'),
]
