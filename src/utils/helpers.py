from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from ..resources.testdata.user_data import user_data
import time

class WebUtils():

    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def open_url(self):
        url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/"
        self.driver.get(url)
        self.driver.implicitly_wait(5)

    # email, password를 입력해서 로그인하는 함수
    def login(self):
        btn_login = self.driver.find_element(By.XPATH, '//button[contains(@class, "bg-main")]')
        btn_login.click()

        input_email = self.driver.find_element(By.ID, 'username')
        input_email.send_keys(user_data["email"])
        input_password = self.driver.find_element(By.ID, 'password')
        input_password.send_keys(user_data["password"])

        btn_submit = self.driver.find_element(By.NAME, 'action')
        btn_submit.click()

        return self.driver.get_cookies()

    # 쿠키를 입력해서 자동 로그인하는 함수
    # login() 1회 실행 후 return되는 쿠키값 클래스변수에 넣어두면 단위테스트할때 자동 로그인 가능
    def login_auto(self, cookies: list):
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        time.sleep(2)