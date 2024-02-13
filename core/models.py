from django.db import models


class ActivateMixin(models.Model):
    is_active = models.BooleanField(default=False)

    class Meta:
        abstract = True


class TimeStampMixin(models.Model):
    updated_at = models.DateTimeField(editable=False, auto_now=True)
    created_at = models.DateTimeField(editable=False, auto_now_add=True)

    class Meta:
        abstract = True
