import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.utils.helpers import WebUtils
from src.resources.testdata.user_data import signin_data

class LoginPage(WebUtils):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def input_email(self, by, value, email):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by, value))
        )
        element.send_keys(email)

    def input_password(self, by, value, password):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by, value))
        )
        element.send_keys(password)

    def input_text(self, by, value, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by, value))
        )
        element.send_keys(text)

    # 프로필 팀 선택
    def click_team(self, by, value, team):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((by, value))
        ).click()
        
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'option[value="디자인 1팀"]'))
        ).click()
        