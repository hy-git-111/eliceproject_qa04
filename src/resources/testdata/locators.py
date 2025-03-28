from selenium.webdriver.common.by import By

LOCATORS = {
    # [로그인 페이지]
    # "login_pg_title_section": (By.CSS_SELECTOR, 'div.mb-8'),
    "login_pg_title": (By.CSS_SELECTOR, 'h1.mb-2'),
    "login_pg_title_sub": (By.CSS_SELECTOR, 'p.text-gray-600'),

    "login_pg_login_btn": (By.CSS_SELECTOR, 'button.bg-main'),
    "login_pg_signin_btn": (By.CSS_SELECTOR, 'button.bg-sub'),

    # [로그인 정보 입력 페이지]
    # "login_input_pg_title_section": (By.CSS_SELECTOR, 'header.c825c97f8'),
    "login_input_pg_title": (By.CSS_SELECTOR, 'h1.ca90b15ee'),
    "login_input_pg_title_sub": (By.CSS_SELECTOR, 'body > div > main > section > div > div > header > div.ced95a2c2.ca6c299fa > p'),

    "login_input_pg_input_email": (By.ID, 'username'),
    "login_input_pg_input_pwd": (By.ID, 'password'), 
    "login_input_pg_placeholder_email": (By.CSS_SELECTOR, 'div[data-dynamic-label-for~="username"]'),
    "login_input_pg_placeholder_pwd": (By.CSS_SELECTOR, 'div[data-dynamic-label-for~="password"]'),

    "login_input_pg_link_reset_pwd": (By.CSS_SELECTOR, 'a.c7c6decd9'),
    "login_input_pg_link_signin": (By.CSS_SELECTOR, 'body > div > main > section > div > div > div > div > p > a'),
    "login_input_pg_btn_continue": (By.CSS_SELECTOR, 'button.cc02a3617'),
    
    # [비밀번호 초기화 페이지]
    "pwd_reset_pg_title": (By.CSS_SELECTOR, 'h1.ca90b15ee.c2bb004c2'),
    "pwd_reset_pg_title_sub": (By.CSS_SELECTOR, 'p.c53c6f72a'),

    "pwd_reset_pg_input_email": (By.ID, 'email'),
    "pwd_reset_pg_placeholder_email": (By.CSS_SELECTOR, 'div.cd61d9fdd.js-required'),

    "pwd_reset_pg_btn_continue": (By.CSS_SELECTOR, 'button.c1085a438'),
    "pwd_reset_pg_link_login": (By.CSS_SELECTOR, 'button._link-back-to-login'),

    #[이메일 전송 완료 페이지]
    "send_mail_pg_title": (By.CSS_SELECTOR, 'h1.c2b7602e3'),
    "send_mail_pg_title_sub": (By.CSS_SELECTOR, 'p.c53c6f72a'),

    "send_mail_pg_btn_resend": (By.CSS_SELECTOR, 'button.c20d4b85c'),

    # [회원가입 페이지]
    "signin_pg_title": (By.CSS_SELECTOR, 'h1.ca90b15ee'),
    "signin_pg_title_sub": (By.CSS_SELECTOR, 'body > div > main > section > div > div > header > div.ced95a2c2.ca6c299fa > p'),

    "signin_pg_input_email": (By.ID, 'email'),
    "signin_pg_input_pwd": (By.ID, 'password'),
    "signin_pg_placeholder_email": (By.CSS_SELECTOR, 'div[data-dynamic-label-for~="email"]'),
    "signin_pg_placeholder_pwd": (By.CSS_SELECTOR, 'div[data-dynamic-label-for~="password"]'),

    "signin_pg_pg_btn_continue": (By.CSS_SELECTOR, 'button.c1085a438'),
    "signin_pg_link_login": (By.CSS_SELECTOR, 'a.c61ec4995'),

# 작성중
    # "signin_pg_pw_rule_title": (By.)
    # "signin_pg_pw_rule_num_of_char": (By.)
}
EXPECTED_TEXTS = {
    # [로그인 페이지]
    "login_pg_title": "오늘 뭐 먹지?",
    "login_pg_title_sub": "오늘의 식사 메뉴를 추천해드립니다",

    # [로그인 정보 입력 페이지]
    "login_input_pg_placeholder_email": "오늘 뭐 먹지?",
    "login_input_pg_placeholder_pwd": "맛있는 선택은 당신의 하루를 바꿉니다.",

    # [비밀번호 초기화 페이지]
    "pwd_reset_pg_title": "비밀번호를 잊어버리셨나요?",
    "pwd_reset_pg_title_sub": "이메일 주소를 입력하면 비밀번호 재설정 지침을 보내드립니다.",
    "pwd_reset_pg_placeholder_email": "이메일 주소*",
    "pwd_reset_pg_link_login": "로그인 화면으로 돌아가기",

    #[이메일 전송 완료 페이지]
    "send_mail_pg_title": "Check Your Email",
    "send_mail_pg_title_sub": "Please check the email address hyeyoung.k111@gmail.com for instructions to reset your password.",
    
    # [회원가입 페이지]
    "signin_pg_title": "환영합니다",
    "signin_pg_title_sub": "오늘 뭐 먹지? 를 사용하시려면 회원가입을 진행해주세요.",
    "signin_pg_placeholder_email": "이메일 주소*",
    "signin_pg_placeholder_pwd": "비밀번호*",




}
