from django.test import TestCase

from .models import Order, OrderItem, get_user_model

User = get_user_model()


class OrderTestCase(TestCase):
    def setUp(self):
        print(User.objects.all())
        self.owner = User.objects.create_user(phone="09126667722", password="1234")
        print(User.objects.all())
        print("Setup called :)")

    # def test1_create_order(self):
    #     order = Order.objects.create(owner=self.owner)
    #     self.assertEqual(order.id, 1)
    #
    # def test2_unittest_life_cycle(self):
    #     self.assertRaises(Exception, Order.objects.get, id=1)  # noqa

    # TDD:
    # def test1_initialize_order_model(self):
        # order -> (is_paid = False, owner : User)


        # self.assertTrue(hasattr(Order, "is_paid"))
        # self.assertTrue(hasattr(Order, "owner"))
        #
        # self.assertRaises(Exception, Order.objects.create)
