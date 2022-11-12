from django.urls import path
from . import views

urlpatterns = [
    path('users', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('posts', views.PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetaile.as_view(), name='user-detail'),
    path('comments/',views.CommentList.as_view()),
    path('comments/<int:pk>/',views.CommentDetail.as_view()),
    path('categorys/',views.CategoryList.as_view()),
    path('categorys/<int:pk>/',views.CategoryDetail.as_view())
]
