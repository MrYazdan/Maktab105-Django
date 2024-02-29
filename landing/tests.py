from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from django.contrib.staticfiles.testing import LiveServerTestCase


User = get_user_model()


# Create your tests here.
class ViewTestCase(TestCase):
    def test1_client(self):
        response = self.client.get("/")
        print(response.__dict__)
        self.assertContains(response, "| Home")

    # def test2_auth_view(self):
    #     self.assertRaises(User.DoesNotExist, User.objects.get, id=1)
    #     self.client.post("/register", data={
    #         "phone": "09123457788",
    #         "password": "1234"
    #     })
    #
    #     self.assertTrue(User.objects.filter(id=1).exists())
    #
    #     response = self.client.post("/login", data={
    #         "phone": "09123457788",
    #         "password": "1234"
    #     })
    #
    #     print(self.client.user)


class AuthTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions())
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test1_register(self):
        self.selenium.get(self.live_server_url + "/register")
        import time

        phone_input = self.selenium.find_element(By.CSS_SELECTOR,"input[name=phone]")
        phone_input.send_keys("09137778888")

        time.sleep(5)

        password_input = self.selenium.find_element(By.CSS_SELECTOR,"input[name=password]")
        password_input.send_keys("1")

        self.selenium.find_element(By.CSS_SELECTOR, "form:not(#searchForm) > input[type=submit]").click()

        time.sleep(5)

        username_input = self.selenium.find_element(By.CSS_SELECTOR,"input[name=username]")
        username_input.send_keys("09137778888")

        time.sleep(5)

        password_input = self.selenium.find_element(By.CSS_SELECTOR,"input[name=password]")
        password_input.send_keys("1")

        time.sleep(5)

        self.selenium.find_element(By.CSS_SELECTOR, "form:not(#searchForm) > input[type=submit]").click()

        time.sleep(500)