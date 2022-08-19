from django.urls import path
from match import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.find_date_end, name='match'),
    path('study_detail/<str:id>/', views.study_detail, name='study_detail'),
    path('study_edit/<str:id>/', views.study_edit, name='study_edit'),
    path('study_delete/<str:id>/', views.study_delete, name='study_delete'),
    path('hashtag_write/<str:id>/', views.hashtag_write, name='hashtag_write'),
    path('<int:pk>/', views.hashtag_detail, name = 'hashtag_detail'),
    path('recruit_user/<str:id>/', views.recruit_user, name='recruit_user'),
    path('bookmark/<str:id>/', views.bookmark, name='bookmark'),
    path('comment_edit/<str:id>/<str:comment_id>/', views.comment_edit, name='comment_edit'),
    path('comment_delete/<str:id>/<str:comment_id>/', views.comment_delete, name='comment_delete'),
    path('recomment_write/<str:id>/<str:comment_id>/', views.recomment_write, name='recomment_write'),
    path('study_like/<int:recruit_id>/', views.likes, name='likes'),
    path('sort_by_like',views.sort_by_like,name = 'sort_by_like'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)