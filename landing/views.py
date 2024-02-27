import json

from blog.models import Post
# from blog.forms import PostForm
from django.urls import reverse_lazy
from django.views import View, generic
# from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
# from django.http import HttpResponseBadRequest, HttpResponse


# navbar_items = [
#     {'title': 'Home', 'url': reverse_lazy('landing:home'), 'classes': ""},
#     {'title': 'Posts', 'url': reverse_lazy('landing:posts'), 'classes': ""},
# ]


# fbv -> function based view
# def home(req):
#     return render(req, "home.html", {"navbar_items": navbar_items, 'title': 'Home'})
#
#
# def posts(request):
#     return render(request, "posts.html", {
#         'posts': Post.objects.all(),
#         'title': 'Posts',
#         "navbar_items": navbar_items
#     })

# cbv -> class based view
# class BaseView(View):
#     base_context = {
#         # 'navbar_items': [
#         #     {'title': 'Home', 'url': reverse_lazy('landing:home'), 'classes': ""},
#         #     {'title': 'Posts', 'url': reverse_lazy('landing:posts'), 'classes': ""},
#         # ]
#     }


# class HomeView(BaseView):
#     def get(self, request):
#         return render(self.request, "home.html", {**self.base_context})
#
#     def post(self, request):
#         return JsonResponse({'status': 200, 'msg': "Post daryaf shod !"})


# class PostView(BaseView):
#     # ListCreateView() :)
#     _form_class = PostForm
#
#     def get(self, request):
#         return render(self.request, "posts.html", {
#             'posts': Post.objects.all(),
#             'form': self._form_class(),
#             **self.base_context
#         })
#
#     def post(self, request):
#         form = self._form_class(self.request.POST)
#
#         if form.is_valid():
#             form.save()
#
#             return HttpResponse("Created :)")
#         return HttpResponseBadRequest('Form invalid')


# class PostDetail(BaseView):
#     def get(self, request, pk):
#         post = get_object_or_404(Post, id=pk)
#         return render(self.request, "post.html", {'post': post, **self.base_context})
#
#     def delete(self, request, pk):
#         post = get_object_or_404(Post, pk=self.kwargs['pk'])
#         post.delete()
#
#         return JsonResponse({"status": 200, "redirect": reverse_lazy("landing:posts")})


# cbv -> generics:
# class BaseContextMixin(generic.base.ContextMixin):
#     base_context = {
#         'navbar_items': [
#             {'title': 'Home', 'url': reverse_lazy('landing:home'), 'classes': ""},
#             {'title': 'Posts', 'url': reverse_lazy('landing:posts'), 'classes': ""},
#         ]
#     }
#
#     def get_context_data(self, **kwargs):
#         default_context = super().get_context_data(**kwargs)
#         return {**default_context, **self.base_context}


class PostView(generic.CreateView):
    model = Post
    fields = ["title", "author", "content"]
    success_url = reverse_lazy("landing:posts")
    template_name = "posts.html"


class PostDetail(generic.DetailView, generic.DeleteView):
    template_name = "post.html"
    model = Post
    success_url = reverse_lazy("landing:posts")


class AjaxPostListView(View):
    def get(self, request):
        return JsonResponse(data=[*Post.objects.values('id', 'title', 'author__username', 'content')], safe=False)


class AjaxPostFilterView(View):
    def get(self, request, name):
        import time
        time.sleep(10)  
        return JsonResponse(data=[*Post.objects.filter(title__icontains=name)
                            .values('id', 'title', 'author__username', 'content')], safe=False)

