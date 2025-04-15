from django.urls import path
from .views import TaskListView, TaskCreateView, register, TaskUpdateView, toggle_task

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),  # Homepage
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('register/', register, name='register'),  # New registration URL
    path('edit/<int:pk>/', TaskUpdateView.as_view(), name='task-edit'),
    path('accounts/signup/', register, name='signup'),  # Moved to accounts/
    path('toggle/<int:pk>/', toggle_task, name='task-toggle'),
    
]
