from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["status", "-created_at"]

    def __str__(self):
        return f"#{self.id}"

    @property
    def is_done(self):
        return self.status is True

    @property
    def status_str(self):
        variables = {True: "Done", False: "Not done"}
        return variables[self.status]

    @property
    def tags_str(self) -> str:
        return " ".join(tag.name for tag in self.tags.all())
