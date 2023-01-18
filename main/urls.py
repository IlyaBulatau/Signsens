from django.urls import path, include

from main import views

urlpatterns = [
    path('', views.start_page, name='start_page'),
    path('welcom/', views.welcom, name='welcom'),
    path('main/', views.main, name='main')
]