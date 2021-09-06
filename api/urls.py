from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    #path('posts/', views.PostList.as_view()),
    path('posts/', views.posts),
    path('posts/<int:pk>/', views.post_details),
]

urlpatterns = format_suffix_patterns(urlpatterns)