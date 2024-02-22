# from .views import home, posts
# from .views import HomeView, Posts, PostDetail
from .views import PostView, PostDetail
from django.urls import path
from django.views.generic import TemplateView

app_name = "landing"
urlpatterns = [
    # path('', home, name="home"),
    # path('posts/', posts, name="posts"),

    # cbv
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('posts/', PostView.as_view(), name="posts"),
    path('posts/<int:pk>', PostDetail.as_view(), name="post_detail"),
]
