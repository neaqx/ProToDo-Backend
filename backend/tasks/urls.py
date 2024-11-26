from django.urls import path
from .views import TaskListCreateView, TaskDetailView, CategoryView, CommentListCreateView, CommentDetailView

urlpatterns = [
  
    path('tasks/', TaskListCreateView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),

    path('categories/', CategoryView.as_view(), name='category-list'),
  
    path('tasks/<int:task_id>/comments/', CommentListCreateView.as_view(), name='task-comments'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]
