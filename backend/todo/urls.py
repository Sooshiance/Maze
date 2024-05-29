from django.urls import path

from todo.views import (
    AllTaskAPIView, SingleTaskAPIView, CreateTaskAPIView, DeleteTaskAPIView
)


urlpatterns = [
    path('tasks/', AllTaskAPIView.as_view(), name='all-tasks'),
    path('tasks/<int:pk>/', SingleTaskAPIView.as_view(), name='task'),
    path('task/create/', CreateTaskAPIView.as_view(), name='create-task'),
    path('task/delete/<int:pk>/', DeleteTaskAPIView.as_view(), name='delete-task'),
]
