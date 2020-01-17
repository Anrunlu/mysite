from django.urls import path
from . import views

# blog/
urlpatterns = [
    path('update_comment', views.update_comment, name='update_comment'),
]
