from django.db import models
from core.models import TimeStampMixin, ActivateMixin


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    # def all(self):
    #     return self.filter()
    #
    # def exclude(self, *args, **kwargs):
    #     return super().exclude(*args, **kwargs)
    #
    # def filter(self, *args, **kwargs):
    #     return super().filter(*args, **kwargs).filter(is_active=True)

    def inactivates(self):
        return super().get_queryset().filter(is_active=False)


class Comment(TimeStampMixin, ActivateMixin):
    author = models.CharField(max_length=100)
    comment = models.TextField()

    # managers
    # objects = models.Manager()
    # actives = ActiveManager()
    objects = ActiveManager()


class Product(TimeStampMixin, ActivateMixin):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()


class OrderedProduct(Product):
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created_at", "-price"]
        proxy = True


class Image(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=20)
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()


class Slide(Image):
    # image = models.OneToOneField(Image, on_delete=models.CASCADE, primary_key=True)
    link = models.URLField()
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=70)
    slider = models.ForeignKey('Slider', models.CASCADE)


class Slider(models.Model):
    name = models.CharField(max_length=80)
