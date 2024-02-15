from django.db import models

from shop.managers import LogicalProductManager


class ActiveMixin(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class DeleteMixin(models.Model):
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class LogicalProductMixin(ActiveMixin, DeleteMixin):

    # manager:
    objects = LogicalProductManager()

    class Meta:
        abstract = True
