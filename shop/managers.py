from django.db import models


class LogicalQuerySet(models.QuerySet):
    def delete(self):
        return super().update(is_deleted=True)


class LogicalProductManager(models.Manager):
    def get_queryset_object(self):
        if not hasattr(self.__class__, '__queryset'):
            self.__class__.__queryset = LogicalQuerySet(self.model)

        return self.__queryset

    def get_queryset(self):
        return self.get_queryset_object().filter(is_active=True, is_deleted=False)

    def archive(self):
        return super().get_queryset()
