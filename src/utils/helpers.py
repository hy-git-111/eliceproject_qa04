import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.webdriver import WebDriver

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
