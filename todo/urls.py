from django.urls import path
from .views import (
    TaskView,
    TagView,
    TaskCreateView,
    TaskDeleteView,
    TagCreateView,
    TagDeleteView,
    TagUpdateView,
    TaskUpdateView,
    toggle_complete
)

urlpatterns = [
    path("", TaskView.as_view(), name="task_list"),

    path("tags/", TagView.as_view(), name="tag_list"),
    path("tag/create/", TagCreateView.as_view(), name="tag_create"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag_update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag_delete"),

    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),

    path("<int:pk>/toggle/", toggle_complete, name="task_toggle"),
]

app_name = "todo"
