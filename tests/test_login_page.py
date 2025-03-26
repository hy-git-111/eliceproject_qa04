from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.utils.helpers import WebUtils
from src.pages.login_page import LoginPage
from src.resources.testdata.report_path import screenshot
from src.resources.testdata.user_data import user_data
import time
import pytest


class TestLoginPage:
# [로그인 페이지] UI 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_001(self):
        try:
            driver = webdriver.Chrome()
            web_utils = WebUtils(driver)

            web_utils.open_url()
            time.sleep(2)

            title = driver.find_element(By.TAG_NAME, 'h1')
            title_sub = driver.find_element(By.CLASS_NAME, 'text-gray-600')
            btn_login = driver.find_element(By.XPATH, '//button[contains(@class, "bg-main")]')
            btn_signin = driver.find_element(By.XPATH, '//button[contains(@class, "bg-sub")]')

            assert title.text == "오늘 뭐 먹지?"
            assert title_sub.text == "오늘의 식사 메뉴를 추천해드립니다"
            assert btn_login != None
            assert btn_signin != None
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-001_성공.png")

        except NoSuchElementException as e:
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-001_실패_NoSuchElementException.png")

        except TimeoutException as e:
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-001_실패_TimeoutException.png")

# [로그인 정보 입력 페이지] UI확인
    @pytest.mark.skip(reason="test pass")
    def test_login_002(self):
        try:
            driver = webdriver.Chrome()
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)

            web_utils.open_url()
            time.sleep(2)

            login_page.click_btn_include_class_name("bg-main")

            title = driver.find_element(By.TAG_NAME, 'h1')
            title_sub = title.find_element(By.XPATH, './/following-sibling::div/p')

            input_email = driver.find_element(By.ID, 'username')
            placeholder_email = driver.find_element(By.XPATH, '//div[@data-dynamic-label-for="username"]')

            input_password = driver.find_element(By.ID, 'password')
            placeholder_password = driver.find_element(By.XPATH, '//div[@data-dynamic-label-for="password"]')
            password_masked = input_password.get_attribute("type")

            link_text_reset_password = driver.find_element(By.XPATH, '//a[contains(@class, "c7c6decd9")]')
            link_text_signin = driver.find_element(By.CSS_SELECTOR, 'body > div > main > section > div > div > div > div > p > a')
            btn_continue = driver.find_element(By.XPATH, '//button[contains(@class, "cc02a3617")]')

            assert title.text == "오늘 뭐 먹지?"
            assert title_sub.text == "맛있는 선택은 당신의 하루를 바꿉니다."

            assert input_email != None
            assert placeholder_email.text.strip() == "이메일 주소*"

            assert input_password != None
            assert placeholder_password.text.strip() == "비밀번호*"
            assert password_masked == "password"

            assert link_text_reset_password.text == "비밀번호를 잊으셨나요?"
            assert link_text_signin.text == "회원가입"
            assert btn_continue != None
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-002_성공.png")

        except NoSuchElementException as e:
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-002_실패_NoSuchElementException.png")

        except TimeoutException as e:
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-002_실패_TimeoutException.png")

# [비밀번호 초기화 페이지] UI 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_003(self):
        try:
            driver = webdriver.Chrome()
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)

            web_utils.open_url()
            time.sleep(2)

            # "로그인 하기 버튼" 클릭
            login_page.click_btn_include_class_name("bg-main")

            # '비밀번호를 잊으셨나요? 링크' 클릭
            login_page.click_link_include_class_name("c7c6decd9")

            title = driver.find_element(By.TAG_NAME, 'h1')
            title_sub = title.find_element(By.XPATH, './/following-sibling::div/p')

            input_email = driver.find_element(By.ID, 'email')
            placeholder_email = driver.find_element(By.XPATH, '//div[@data-dynamic-label-for="email"]')

            btn_continue = driver.find_element(By.XPATH, '//button[contains(@class, "c1085a438")]')
            link_text_go_to_login = driver.find_element(By.XPATH, '//button[contains(@class, "_link-back-to-login")]')

            assert title.text == "비밀번호를 잊어버리셨나요?"
            assert title_sub.text == "이메일 주소를 입력하면 비밀번호 재설정 지침을 보내드립니다."

            assert input_email != None
            assert placeholder_email.text.strip() == "이메일 주소*"

            assert btn_continue != None
            assert link_text_go_to_login.text == "로그인 화면으로 돌아가기"

            assert "reset-password/request" in driver.current_url
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-003_성공.png")

        except NoSuchElementException as e:
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-003_실패_NoSuchElementException.png")

        except TimeoutException as e:
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-003_실패_TimeoutException.png")

# [이메일 전송 완료 페이지] UI 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_004(self):
        try:
            driver = webdriver.Chrome()
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)

            web_utils.open_url()
            time.sleep(2)

            # "로그인 하기 버튼" 클릭
            login_page.click_btn_include_class_name("bg-main")

            # '비밀번호를 잊으셨나요? 링크' 클릭
            login_page.click_link_include_class_name("c7c6decd9")
            time.sleep(2)

            # 이메일 전송
            login_page.input_email(user_data["email"])
            login_page.click_btn_include_class_name("c1085a438")
            time.sleep(2)

            title = driver.find_element(By.TAG_NAME, 'h1')
            title_sub = title.find_element(By.XPATH, './/following-sibling::p')
            btn_resend = driver.find_element(By.XPATH, '//button[contains(@class, "c20d4b85c")]')

            assert title.text == "Check Your Email"
            assert title_sub.text == "Please check the email address hyeyoung.k111@gmail.com for instructions to reset your password."
            assert btn_resend.text == "Resend email"
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-004_성공.png")

        except NoSuchElementException as e:
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-004_실패_NoSuchElementException.png")

        except TimeoutException as e:
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-004_실패_TimeoutException.png")

# TC LOGIN-005 누락

# [로그인 페이지] 진입 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_010(self):
        try:
            driver = webdriver.Chrome()
            web_utils = WebUtils(driver)

            web_utils.open_url()
            time.sleep(2)

            assert "signin" in driver.current_url
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-010_성공.png")

        except NoSuchElementException as e:
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-010_실패_NoSuchElementException.png")

        except TimeoutException as e:
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-010_실패_TimeoutException.png")

# [로그인 정보 입력 페이지] 진입 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_011(self):
        try:
            driver = webdriver.Chrome()
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)

            web_utils.open_url()
            time.sleep(2)

            # "로그인 하기 버튼" 클릭
            login_page.click_btn_include_class_name("bg-main")

            assert "login?" in driver.current_url
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-011_성공.png")

        except NoSuchElementException as e:
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-011_실패_NoSuchElementException.png")

        except TimeoutException as e:
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-011_실패_TimeoutException.png")

# TC LOGIN-012 ~ LOGIN-013 누락

# [로그인 정보 입력 페이지] 로그인
    @pytest.mark.skip(reason="test pass")
    def test_login_014(self):
        try: 
            driver = webdriver.Chrome()
            web_utils = WebUtils(driver)

            web_utils.open_url()
            time.sleep(2)

            web_utils.login()
            time.sleep(2)

            assert "kdt-pt-1-pj-2-team03.elicecoding.com" in driver.current_url
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-014_성공.png")

        except NoSuchElementException as e:
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-014_실패_NoSuchElementException.png")

        except TimeoutException as e:
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-014_실패_TimeoutException.png")

# [로그인 정보 입력 페이지] 진입 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_015(self):
        try:
            driver = webdriver.Chrome()
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)

            web_utils.open_url()
            time.sleep(2)

            # "로그인 하기 버튼" 클릭
            login_page.click_btn_include_class_name("bg-main")

            # '비밀번호를 잊으셨나요? 링크' 클릭
            login_page.click_link_include_class_name("c7c6decd9")

            assert "reset-password/request" in driver.current_url
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-015_성공.png")

        except NoSuchElementException as e:
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-015_실패_NoSuchElementException.png")

        except TimeoutException as e:
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-015_실패_TimeoutException.png")

# TC LOGIN-016 누락

# 이메일 재 전송
    @pytest.mark.skip(reason="test fail")
    def test_login_017(self):
        try:
            driver = webdriver.Chrome()
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)

            web_utils.open_url()
            time.sleep(2)

            # "로그인 하기 버튼" 클릭
            login_page.click_btn_include_class_name("bg-main")

            # '비밀번호를 잊으셨나요? 링크' 클릭
            login_page.click_link_include_class_name("c7c6decd9")
            time.sleep(2)

            # 이메일 전송
            login_page.input_email(user_data["email"])
            time.sleep(2)
            login_page.click_btn_include_class_name("c1085a438")
            time.sleep(2)

            # 이메일 재 전송
            login_page.click_btn_include_class_name("c1085a438")
            
            input_email = driver.find_element(By.ID, 'email')
            input_value = input_email.get_attribute("value")

            assert input_value == ""
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-017_성공.png")

        except NoSuchElementException as e:
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-017_실패_NoSuchElementException.png")

        except TimeoutException as e:
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-017_실패_TimeoutException.png")

# TC LOGIN-018 ~ LOGIN-019 누락

# [비밀번호 초기화 페이지]에서 [로그인 정보 입력 페이지] 진입 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_020(self):
        try:
            driver = webdriver.Chrome()
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)

            web_utils.open_url()
            time.sleep(2)

            # "로그인 하기 버튼" 클릭
            login_page.click_btn_include_class_name("bg-main")
            time.sleep(2)

            # '비밀번호를 잊으셨나요? 링크' 클릭
            login_page.click_link_include_class_name("c7c6decd9")
            time.sleep(2)

            # '로그인 화면으로 돌아가기 링크' 클릭
            # login_page.click_link_include_class_name("c61ec4995")
            login_page.click_btn_go_to_login()
            time.sleep(2)

            assert "login?" in driver.current_url
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-020_성공.png")

        except NoSuchElementException as e:
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-020_실패_NoSuchElementException.png")

        except TimeoutException as e:
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-020_실패_TimeoutException.png")

# [로그인 정보 입력 페이지]에서 [회원가입 페이지]로 이동 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_021(self):
        try:
            driver = webdriver.Chrome()
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)

            web_utils.open_url()
            time.sleep(2)

            # "로그인 하기 버튼" 클릭
            login_page.click_btn_include_class_name("bg-main")
            time.sleep(2)

            # '회원가입 링크' 클릭
            login_page.click_btn_go_to_signin()
            time.sleep(2)

            assert "signup?" in driver.current_url
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-021_성공.png")

        except NoSuchElementException as e:
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-021_실패_NoSuchElementException.png")

        except TimeoutException as e:
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-021_실패_TimeoutException.png")

# [로그인 페이지]에서 [회원가입 페이지] 진입 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_022(self):
        try:
            driver = webdriver.Chrome()
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)

            web_utils.open_url()
            time.sleep(2)

            # '회원가입 버튼' 클릭
            login_page.click_btn_include_class_name("bg-sub")
            time.sleep(20)

            assert "signup?" in driver.current_url
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-022_성공.png")

        except NoSuchElementException as e:
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-022_실패_NoSuchElementException.png")

        except TimeoutException as e:
            driver.save_screenshot(f"{screenshot}/로그인페이지_LOGIN-022_실패_TimeoutException.png")
