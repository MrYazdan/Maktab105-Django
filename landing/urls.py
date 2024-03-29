# from .views import home, posts
# from .views import HomeView, Posts, PostDetail
from django.http import JsonResponse

from blog.models import Post
from .views import PostView, PostDetail, AjaxPostListView, AjaxPostFilterView
from django.urls import path
from django.views.generic import ListView


def json_view(request):
    return JsonResponse({
        "maktab": 105
    })


app_name = "landing"
urlpatterns = [
    # path('', home, name="home"),
    # path('posts/', posts, name="posts"),

    # cbv
    path('', ListView.as_view(
        queryset=Post.objects.all(),
        template_name="home.html",
        context_object_name="posts"
    ), name="home"),
    path('posts/', PostView.as_view(), name="posts"),
    path('json/', json_view, name="json"),
    path('ajax/posts/', AjaxPostListView.as_view(), name="posts"),
    path('ajax/posts/filter/<str:name>', AjaxPostFilterView.as_view(), name="posts"),
    path('posts/<int:pk>', PostDetail.as_view(), name="post_detail"),
]
