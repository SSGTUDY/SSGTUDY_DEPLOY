from django.urls import path
from match import views

urlpatterns = [
    path('', views.match, name='match'),
    path('study_detail/', views.study_detail, name='study_detail'),
    path('study_edit/', views.study_edit, name='study_edit'),
    path('study_delete', views.study_delete, name='study_delete'),
]