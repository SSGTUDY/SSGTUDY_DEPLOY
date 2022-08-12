from django.urls import path
from about import views


urlpatterns = [
    # about
    path('', views.about_main, name='about_main'),
    path('manual/', views.about_manual, name='about_manual'),
    path('main/', views.about_main, name='about_main'),
    path('post/', views.about_post, name='about_post'),
    path('notice/', views.about_notice, name='about_notice'),
    path('qna/', views.about_qna, name='about_qna'),
    path('person/', views.about_person, name='about_person'),
]