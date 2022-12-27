from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True)
    tags = models.ManyToManyField(Tag, related_name="tasks")
    complete = models.BooleanField(default=False, blank=True)

    class Meta:
        ordering = ("complete", "-date")

    def __str__(self):
        return f"{self.title} {self.date} {self.deadline} {self.tags}"
