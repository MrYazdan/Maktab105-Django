import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from blog.models import Post, User  # noqa

# yazdan = User.objects.create(username="yazdan")
# Post.objects.create(title="Python good", author=yazdan)

# print(*Post.objects.all(), sep="\n")
# print(Post.objects.all())

# yazdan = User.objects.get(username='yazdan')
# Post.objects.create(title="Java good", author=yazdan)
# Post.objects.create(title="Php good", author=yazdan)
# Post.objects.create(title="Perl good", author=yazdan)
#
# pedram = User.objects.create(username='pedram')
# Post.objects.create(title="Bash bad", author=pedram)
# Post.objects.create(title="C++ bad", author=pedram)

yazdan = User.objects.get(username='yazdan')
pedram = User.objects.get(username='pedram')

# print(type(User.objects.get(username="yazdan")))
# print(isinstance(User.objects.get(username="yazdan"), User))
# print(Post.objects.filter(author__id=5))

# 1: get -> try:
# try:
#     my_user = User.objects.get(username="my_user")
# except User.DoesNotExist:
#     print("My User Does Not Exists!")

# 2: get -> filter
# my_user = User.objects.filter(username="my_user")
# print(my_user.query)
# assert my_user, "My User Does Not Exists!"

# 3: get -> filter + exists
# my_user = False
# if User.objects.filter(username="yazdan").exists():
#     my_user = User.objects.filter(username="yazdan")[0]

# my_user = (queryset := User.objects.filter(username="yazdan")).exists() and queryset[0]
# print(my_user)

# assert my_user, "My User Does Not Exists!"

# 4: get -> 404 in view
# from django.shortcuts import get_object_or_404
# print(get_object_or_404(User, username="yazdani"))

# Yazdan Posts =>

# 1:
# print(Post.objects.filter(author=yazdan))

# 2:
# print(yazdan.post_set.all())

# 3:
# set related_name = "posts"
# print(yazdan.posts.all())

print(getattr(yazdan, 'posts').all())
print(hasattr(yazdan, 'posts'))
