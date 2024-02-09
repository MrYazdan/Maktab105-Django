from blog.views import home, posts
from django.urls import path,include
from django.contrib import admin

urlpatterns = [
    path('', home, name="home"),
    path('posts/', posts, name="posts"),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
]
