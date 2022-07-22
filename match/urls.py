from django.urls import path
from match import views

urlpatterns = [
    path('', views.match, name='match'),
    path('study_detail/', views.study_detail, name='study_detail'),
]