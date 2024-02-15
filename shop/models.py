from django.db import models
from core.models import TimeStampMixin
from shop.mixins import LogicalProductMixin


class Product(TimeStampMixin, LogicalProductMixin):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.PositiveSmallIntegerField()

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    def hard_delete(self):
        return super().delete()

    @property
    def title(self):
        return self.name.title()

    def __str__(self):
        return f"<{self.id} - {self.title}>"
