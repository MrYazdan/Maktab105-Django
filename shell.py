import os
from random import randint

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from mixer.backend.django import mixer

# from blog.models import Post, User  # noqa

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

# yazdan = User.objects.get(username='yazdan')
# pedram = User.objects.get(username='pedram')

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

# my_user = (queryset := User.objects.filter(username="yazdan")) and queryset[0]
# print("User:", my_user)

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

# print(getattr(yazdan, 'posts').all())
# print(hasattr(yazdan, 'posts'))

# ------------- S4 --------------

from product.models import Comment, Product, OrderedProduct

# Comment.objects.create(author="fardin", comment="python is good")
# Comment.objects.create(author="zahra", comment="java !!!")
# Comment.objects.create(author="alireza", comment="Good")
# Comment.objects.create(author="yazdan", comment="Ilove BashScript :)")

# print("All: ", Comment.objects.filter())
# print("Actives: ", Comment.actives.filter())
# print("All: ", Comment.objects.all())
# print("Actives: ", Comment.actives.all())

# print(Comment.objects.filter(id__lt=5))
# print(Comment.actives.filter(id__lt=5))

# print(Comment.objects.all())
# print(Comment.objects.inactivates())
# print(Comment.objects.exclude())
# print(Comment.objects.get(id=2))

# print(OrderedProduct.objects.all())

from product.models import Image, Slide, Slider

# main_slider = Slider.objects.create(name="main slider")
# mixer.cycle(9).blend(Slider)

# image_one = Image.objects.create(
#     url="https://google.com",
#     name="Googooli",
#     width=1024,
#     height=768
# )
#
# slide_one = Slide.objects.create(
#     image=image_one,
#     link="https://links.com",
#     title="My Image :)",
#     description="bikhial !",
#     slider=main_slider
# )

# print(*Slide._meta.get_fields(), sep="\n")

# slider = Slider.objects.get(id=2)
# new_slide = Slide.objects.create(
#     url="https://googooli.go",
#     name="image name",
#     width=1024,
#     height=768,
#     link="/product/35",
#     title="Please subscribe me !",
#     description="this is desc",
#     slider=slider
# )

# from random import randint
#
# for slider in Slider.objects.all():
#     mixer.cycle(randint(1, 20)).blend(Slide, slider=slider)

# Slider.objects.get(id=10).delete()

# ------------- S6 --------------

from shop.models import Product

# mixer.cycle(40).blend(Product)

# print(*Product.objects.all(), sep="\n")

# for p in Product.objects.all():
#     p.is_deleted = bool(randint(0, 1))
#     p.save()

# print(*Product.objects.all(), sep="\n")
# print(*Product.objects.archive(), sep="\n")

# print(Product.objects.get(id=20))
# print(Product.objects.filter(id__gte=15))
# Product.objects.filter(id__gt=17).delete()

# print(Product.objects.archive().update(is_deleted=False))

Product.objects.filter(id__gt=35).delete()
