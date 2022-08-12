from django.urls import path
from mypage import views
from django.conf import settings
from django.conf.urls.static import static
from match import views as match_views


urlpatterns = [
    # mypage_main.js
    path('', views.mypage_main, name='mypage_main'),
    path('mypage_edit/', views.mypage_edit, name='mypage_edit'),
    path('study_register/', views.study_register, name='study_register'),
    path('study_list/', views.my_study_list, name='study_list'),
    path('study_bookmark/', views.study_bookmark, name='study_bookmark'),
    path('study_schedule/', views.study_schedule, name='study_schedule'),
    path('logout/', views.logout, name='logout'),
    path('change_password/',views.change_password,name = 'change_password'),
    path('change_pass/',views.change_pass,name = 'change_pass'),
    path('change_nickname/',views.change_nickname,name = 'change_nickname'),
    path('change_nick/',views.change_nickname,name = "change_nick"),
    path('change_img/',views.change_image,name = 'change_img'),
    path('my_study_list/',views.my_study_list,name = 'my_study_list'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)