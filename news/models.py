from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class Blog(models.Model):
    title = models.CharField(max_length=50, null=False)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("news:detail", kwargs={"pk": self.pk})
    


class BlogHistory(models.Model):
    title = models.CharField(max_length=50, null=False)
    text = models.TextField()
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
