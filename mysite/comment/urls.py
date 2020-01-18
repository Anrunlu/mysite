from django.urls import path
from . import views

# comment/
urlpatterns = [
    path('update_comment', views.update_comment, name='update_comment'),
]
