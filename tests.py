import re
import unittest


class State:
    called_count = 0
    passed_test = 0  # state-full attr


def is_phonenumber(phone: str):
    return re.match(r"^09\d{9}$", phone)


class BuiltinFunctionsTest(unittest.TestCase):
    def setUp(self):
        self.model = State()
        # print("\nSetUp Called :)")

    def tearDown(self):
        # self.model.called_count += 1
        State.called_count += 1
        State.passed_test += 1
        # print("TearDown Called :)")

    def test1_int_list_success(self):
        # import time
        # time.sleep(100)

        self.assertNotEqual(sum([1, -2, 10]), 8, )
        self.assertEqual(self.model.called_count, 0)

    def test2_int_list_success(self):
        # self.assertEqual(self.model.passed_test, 1, "You must passed test 1 !")

        self.assertEqual(sum([1, -2, 10]), 9, "bashe !")
        self.assertEqual(self.model.called_count, 1)

    def test3_isnumeric(self):
        # self.assertEqual(self.model.passed_test, 2, "You must passed test 2 !")

        self.assertTrue("123123".isnumeric())
        self.assertTrue("۱۲۳۱۴۲۳۵۲۴".isnumeric())
        self.assertEqual(self.model.called_count, 2)

    def test4_is_phonenumber(self):
        # self.assertEqual(self.model.passed_test, 3, "You must passed test 3 !")

        self.assertRegex("09123456789", r"^09\d{9}$")
        self.assertEqual(self.model.called_count, 3)


if __name__ == '__main__':
    unittest.main()
