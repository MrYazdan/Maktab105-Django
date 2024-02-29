from django.db import models
from django.core import validators
from django.contrib.auth import get_user_model


class Order(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="orders")
    is_paid = models.BooleanField(default=False)


class OrderItem(models.Model):
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1, validators=[validators.MinValueValidator(1)])
    order = models.ForeignKey("Order", on_delete=models.CASCADE)

    @property
    def price(self):
        return self.count * self.product.price
