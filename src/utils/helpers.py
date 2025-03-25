from selenium.webdriver.chrome.webdriver import WebDriver

class WebUtils():
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def open_url(self):
        url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/"
        self.driver.get(url)
        self.driver.implicitly_wait(5)
