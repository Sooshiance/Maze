from django.urls import path

from todo.views import (
    AllTaskAPIView, SingleTaskAPIView, CreateTaskAPIView, DeleteTaskAPIView, UpdateTaskAPIView
)


urlpatterns = [
    path('tasks/', AllTaskAPIView.as_view(), name='all-tasks'),
    path('task/<int:pk>/', SingleTaskAPIView.as_view(), name='one-task'),
    path('task/create/', CreateTaskAPIView.as_view(), name='create-task'),
    path('task/delete/<int:pk>/', DeleteTaskAPIView.as_view(), name='delete-task'),
    path('task/update/<int:pk>/', UpdateTaskAPIView.as_view(), name='update-task'),
]
