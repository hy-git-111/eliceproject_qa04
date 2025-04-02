from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class HistoryPage():

    def __init__(self, driver: WebDriver):
        self.driver = driver
        
    # helper.py의 함수와 로케이터 value값 다름
    def star_review_four_click(self):
        star_review_four = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[7]/div/div[4]')
        star_review_four.click()