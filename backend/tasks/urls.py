from django.urls import path
from .views import TaskListCreateView, TaskDetailView, CategoryView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('categories/', CategoryView.as_view(), name='category-list'),
]
