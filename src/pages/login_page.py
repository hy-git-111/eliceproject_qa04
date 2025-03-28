from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.utils.helpers import WebUtils
from src.resources.testdata.user_data import user_data

class LoginPage(WebUtils):

    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def click_element(self, by, value):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()

    def input_email(self, by, value):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by, value))
        )
        element.send_keys(user_data["email"])

    def input_password(self, by, value):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by, value))
        )
        element.send_keys(user_data["password"])