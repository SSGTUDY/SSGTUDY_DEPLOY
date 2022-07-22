from django.urls import path
from match import views

urlpatterns = [
    path('', views.match, name='match'),
]