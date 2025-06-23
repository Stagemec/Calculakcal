from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topics', views.topics, name='topics'),
    path('topic/<topic_id>/', views.topics, name='topic'),
    path('new_topic', views.new_topics, name='new_topic'),

]

