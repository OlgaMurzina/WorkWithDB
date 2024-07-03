from django.urls import path
from crud.work_with_db import views

urlpatterns = [
    path('', views.index),
]