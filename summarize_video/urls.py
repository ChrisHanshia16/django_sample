from django.urls import path
from . import views

urlpatterns = [    path('summarize_video/', views.members, name='summarize_video'),]