from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from app.forms import TagForm, TaskForm
from app.models import Task, Tag


class TagListView(generic.ListView):
    model = Tag
    template_name = "app/tag_list.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "app/tag_form.html"
    success_url = reverse_lazy("app:tag_list")


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "app/tag_form.html"
    success_url = reverse_lazy("app:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    form_class = TagForm
    template_name = "app/tag_confirm_delete.html"
    success_url = reverse_lazy("app:tag-list")


class TaskListView(generic.ListView):
    model = Task
    template_name = "app/task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "app/task_form.html"
    success_url = reverse_lazy("app:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "app/task_form.html"
    success_url = reverse_lazy("app:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    form_class = TaskForm
    template_name = "app/task_confirm_delete.html"
    success_url = reverse_lazy("app:task-list")


def change_task_status(request, pk: int) -> HttpResponse:
    change_to = {
        True: False,
        False: True,
    }
    task = get_object_or_404(Task, pk=pk)
    task.status = change_to[task.status]
    task.save()
    return HttpResponseRedirect(reverse_lazy("app:task-list"))
