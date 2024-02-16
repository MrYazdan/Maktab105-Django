from blog.models import Post
from blog.forms import PostForm
from django.views import View
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse


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
class BaseView(View):
    base_context = {
        'navbar_items': [
            {'title': 'Home', 'url': reverse_lazy('landing:home'), 'classes': ""},
            {'title': 'Posts', 'url': reverse_lazy('landing:posts'), 'classes': ""},
        ]
    }


class Home(BaseView):
    def get(self, request):
        return render(self.request, "home.html", {'title': 'Home', **self.base_context})
    #
    # def post(self, request):
    #     return JsonResponse({'status': 200, 'msg': "Post daryaf shod !"})


class Posts(BaseView):
    _form_class = PostForm

    def get(self, request):
        return render(self.request, "posts.html", {
            'posts': Post.objects.all(),
            'title': 'Posts',
            'form': self._form_class(),
            **self.base_context
        })

    def post(self, request):
        form = self._form_class(self.request.POST)

        if form.is_valid():
            form.save()

            return HttpResponse("Created :)")
        else:
            return HttpResponseBadRequest('Form invalid')
