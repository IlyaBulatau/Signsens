from django.urls import path, include

from main import views

urlpatterns = [
    path('', views.start_page, name='start_page'),
    path('welcom/', views.welcom, name='welcom'),
    path('welcom/word/', views.WordView.as_view(), name='word'),
    path('welcom/word/<slug:word_slug>/', views.WordDetailView.as_view(), name='detail_word')
]