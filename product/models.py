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
