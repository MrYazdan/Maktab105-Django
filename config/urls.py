# from blog.views import home, posts
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    # path('', home, name="home"),
    # path('posts/', posts, name="posts"),

    # landing
    path('', include('landing.urls')),

    # auth
    path('', include('account.urls')),

    # admin
    path('admin/', admin.site.urls, name="admin"),

    # path("auth/", include("django.contrib.auth.urls")),


    # admin textarea editor
    path('tinymce/', include('tinymce.urls')),
]
