from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskForm
from todo.models import Task, Tag


class TaskView(generic.ListView):
    model = Task
    template_name = "todo/todo_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/todo_form.html"
    success_url = reverse_lazy("todo:task_list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/todo_form.html"
    success_url = reverse_lazy("todo:task_list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/todo_delete.html"
    success_url = reverse_lazy("todo:task_list")


class TagView(generic.ListView):
    model = Tag
    template_name = "tag/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "tag/tag_form.html"
    success_url = reverse_lazy("todo:tag_list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "tag/tag_form.html"
    success_url = reverse_lazy("todo:tag_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "tag/tag_delete.html"
    success_url = reverse_lazy("todo:tag_list")


def toggle_complete(request, pk):
    task = Task.objects.get(id=pk)
    task.complete = not task.complete
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo:task_list"))
