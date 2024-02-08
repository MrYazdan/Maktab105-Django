from uuid import uuid4
from django.db import models
from django.utils import timezone

# def id_creator():
#     return uuid4().clock_seq
#
#
# class Temp:
#     id = models.CharField(primary_key=True, max_length=200, default=id_creator)
#     title = models.CharField(max_length=105)


class Post(models.Model):
    title = models.CharField(max_length=105)
    content = models.TextField()

    # datetime as timezone
    # published_time = models.DateTimeField(default=timezone.now)

    # auto_now , auto_now_add
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # relations:
    author = models.ForeignKey("User", on_delete=models.CASCADE, related_name="posts")

    # Python options:
    def __str__(self):
        return f"<Post: {self.id}, title: {self.title}>"

    class Meta:
        # table name:
        db_table = "posts"

        # ordering = ["-id"]


class User(models.Model):
    """
        fields:
          - username

    """

    username = models.CharField(max_length=120)

    # python options:
    def say_hello(self):
        print(f"Hi, {self.username}")

    def __str__(self):
        return self.username
