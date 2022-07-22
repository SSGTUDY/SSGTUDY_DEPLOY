from django.urls import path
from home import views

urlpatterns = [
    # home
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('signup_end/', views.signup_end, name='signup_end'),
]