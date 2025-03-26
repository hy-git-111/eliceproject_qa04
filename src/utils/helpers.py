import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from ..resources.testdata.user_data import user_data

class WebUtils():

    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def open_url(self):
        url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/"
        self.driver.get(url)
        self.driver.implicitly_wait(5)

    def click_back(self):
        back_btn = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/header/div/svg')
        back_btn.click()
        time.sleep(1)

    def click_close(self):
        close_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[1]/button')
        close_btn.click()
        time.sleep(1)

    def click_tab_home(self):
        navigation_bar = self.driver.find_element(By.CSS_SELECTOR, ".bottom-0")
        tab_home = navigation_bar.find_elements(By.TAG_NAME,"a")[0]
        tab_home.click()
        time.sleep(1)

    def click_tab_team(self):
        navigation_bar = self.driver.find_element(By.CSS_SELECTOR, ".bottom-0")
        tab_home = navigation_bar.find_elements(By.TAG_NAME,"a")[1]
        tab_home.click()
        time.sleep(1)

    def click_tab_history(self):
        navigation_bar = self.driver.find_element(By.CSS_SELECTOR, ".bottom-0")
        tab_home = navigation_bar.find_elements(By.TAG_NAME,"a")[2]
        tab_home.click()
        time.sleep(1)

    def click_tab_personal(self):
        navigation_bar = self.driver.find_element(By.CSS_SELECTOR, ".bottom-0")
        tab_home = navigation_bar.find_elements(By.TAG_NAME,"a")[3]
        tab_home.click()
        time.sleep(1)

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
        time.sleep(1)