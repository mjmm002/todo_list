from django.urls import path
from .views import TaskUpdate, DeleteView, TaskList, TaskCreate
from . import views

urlpatterns = [
    path('', TaskList.as_view(), name="list"),
    path('create_task', TaskCreate.as_view(), name="task-create"),
    path('update_task/<str:pk>/', TaskUpdate.as_view(), name="update_task"),
    path('delete/<str:pk>/', DeleteView.as_view(), name="delete")
]