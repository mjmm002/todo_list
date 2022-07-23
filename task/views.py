from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Task
from .forms import TaskForm

# Create your views here.


class TaskList(ListView):
    model = Task
    context_object_name= 'tasks'
    template_name = 'task/list.html'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    template_name= 'task/create_task.html'
    success_url = reverse_lazy('list')



class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('list')
    template_name = 'task/update_task.html'

class DeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'task/delete.html'
    success_url = reverse_lazy('list')