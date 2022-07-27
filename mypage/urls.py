from django.urls import path
from mypage import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # mypage
    path('', views.mypage_main, name='mypage_main'),
    path('mypage_edit/', views.study_register, name='mypage_edit'),
    path('study_register/', views.study_register, name='study_register'),
    path('study_list/', views.study_list, name='study_list'),
    path('study_bookmark/', views.study_bookmark, name='study_bookmark'),
    path('study_schedule/', views.study_schedule, name='study_schedule'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)