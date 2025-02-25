from django.urls import path

from app.views import (
    TaskListView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TaskCreateView,
    change_task_status,
    TagDeleteView,
    TaskDeleteView,
    TaskUpdateView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "tasks/<int:pk>/change-status/", change_task_status, name="task-change-status"
    ),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
]
app_name = "app"
