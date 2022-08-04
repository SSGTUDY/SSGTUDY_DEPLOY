from django.urls import path
from about import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # about
    path('', views.about_main, name='about_main'),
    path('manual/', views.about_manual, name='about_manual'),
    path('notice/', views.about_notice, name='about_notice'),
    path('qna/', views.about_qna, name='about_qna'),
    path('qna_write/', views.about_qna_write, name='about_qna_write'),
    path('qna_detail/<str:id>/', views.about_qna_detail, name='about_qna_detail'),
    path('qna_edit/<str:id>/', views.about_qna_edit, name='about_qna_edit'),
    path('qna_delete/<str:id>/', views.about_qna_delete, name='about_qna_delete'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)