from django.urls import path
from .views import index, topic

urlpatterns = [
    path('', index, name="intro-index"),
    path('topic<str:topic_num>/', topic, name="intro-topic"),
]