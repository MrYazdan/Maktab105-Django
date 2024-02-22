from django.shortcuts import render, redirect
from django.views import generic, View
from django.forms import Form
from django.contrib.auth.views import LoginView as _LoginView, RedirectURLMixin
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate, login, logout

User = get_user_model()


# class LoginView(View):
#     def get(self, request):
#         return render(self.request, 'auth/login.html', context={
#             "form": """
#             <input name="username" required="required" placeholder="please enter your username: "> <br>
#             <input type="password" name="password" required="required" placeholder="please enter your password: "> <br>
#             """
#         })
#
#     def post(self, request):
#         username = self.request.POST.get('username', None)
#         password = self.request.POST.get('password', None)
#
#         assert username and password, "Username or password invalid ..."
#         # print(User.objects.get(id=2).password)
#         # print(User.objects.filter(username=username, password=password))
#
#         # authenticate
#         if user := authenticate(request, username=username, password=password):
#             # login
#             login(request, user)
#             return redirect('landing:home')


class LoginView(_LoginView):
    redirect_authenticated_user = True
    next_page = "landing:home"
    template_name = "auth/login.html"


class LogoutView(generic.RedirectView):
    url = "/"

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(self.request, *args, **kwargs)


class RegisterView(generic.CreateView):
    template_name = "auth/register.html"
    model = User
    fields = ['first_name', 'last_name', 'phone', 'password']
    success_url = "/login"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()

        return super().form_valid(form)

