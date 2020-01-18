from django.urls import path
from . import views

# user/
urlpatterns = [
    path('login_for_modal/', views.login_for_modal, name='login_for_modal'), 
    path('login/', views.login, name='login'), 
    path('register/', views.register, name='register'), 
    path('logout/', views.logout, name='logout'), 
    path('user_info/', views.user_info, name='user_info'), 
]