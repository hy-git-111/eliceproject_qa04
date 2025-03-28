from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.helpers import WebUtils
from src.resources.testdata.user_data import user_data
import time

class LoginPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def click_btn_include_class_name(self, class_name:str):
        btn = self.driver.find_element(By.XPATH, f'//button[contains(@class, "{class_name}")]')
        # btn = self.driver.find_element(By.XPATH, f'//button[contains(@class, hover:bg-main/90)]')
        btn.click()
        
    def click_link_include_class_name(self, class_name1:str, class_name2=None, class_name3=None):
        if class_name2 == None and class_name3 == None:
            link_text = self.driver.find_element(By.XPATH, f'//a[contains(@class, "{class_name1}")]')
            link_text.click()
            return
        
        if class_name2 != None and class_name3 == None:
            link_text = self.driver.find_element(By.XPATH, f'//a[contains(@class, "{class_name1}") and contains(@class, {class_name2})]')
            link_text.click()
            return

        link_text = self.driver.find_element(By.XPATH, f'//a[contains(@class, "{class_name1}") and contains(@class, {class_name2}) and contains(@class, {class_name3})]')
        link_text.click()

    def click_btn_go_to_login(self):
        btn = self.driver.find_element(By.XPATH, '/html/body/div/main/section/div/div/div/div/form/button')
        btn.click()

    def click_btn_go_to_signin(self):
        btn = self.driver.find_element(By.XPATH, '/html/body/div/main/section/div/div/div/div/p/a')
        btn.click()
    
    def input_email(self, email:str):
        input_email = self.driver.find_element(By.ID, 'email')
        input_email.send_keys(email)
