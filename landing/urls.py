# from .views import home, posts
from .views import Home, Posts
from django.urls import path

app_name = "landing"
urlpatterns = [
    # path('', home, name="home"),
    # path('posts/', posts, name="posts"),

    # cbv
    path('', Home.as_view(), name="home"),
    path('posts/', Posts.as_view(), name="posts"),
]
