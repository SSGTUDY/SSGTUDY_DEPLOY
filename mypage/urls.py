from django.urls import path
from mypage import views

urlpatterns = [
    # mypage_main.js
    path('', views.mypage_main, name='mypage_main'),
    path('study_register/', views.study_register, name='study_register'),
    path('study_edit/', views.study_edit, name='study_edit'),
    path('study_list/', views.study_list, name='study_list'),
    path('study_bookmark/', views.study_bookmark, name='study_bookmark'),
    path('study_schedule/', views.study_schedule, name='study_schedule'),
    path('edit/', views.mypage_edit, name='mypage_edit'),
]