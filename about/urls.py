from django.urls import path
from about import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # about
    path('', views.about_main, name='about_main'),
    path('manual/', views.about_manual, name='about_manual'),
    path('notice/', views.about_notice, name='about_notice'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)