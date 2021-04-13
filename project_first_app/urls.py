from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.index),
    path('owners/<int:owner_id>/', detail),
    path('time/', example_view),
]