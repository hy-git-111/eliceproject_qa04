from src.resources.testdata.user_data import signin_data

dynamic_email = signin_data["email"]

EXPECTED_TEXTS = {
    # [로그인 페이지]
    "login_pg_title": "오늘 뭐 먹지?",
    "login_pg_subtitle": "오늘의 식사 메뉴를 추천해드립니다",

    # [로그인 정보 입력 페이지]
    "login_input_pg_title": "오늘 뭐 먹지?",
    "login_input_pg_subtitle": "맛있는 선택은 당신의 하루를 바꿉니다.",
    "login_input_pg_placeholder_email": "이메일 주소*",
    "login_input_pg_placeholder_pwd": "비밀번호*",

    # [비밀번호 초기화 페이지]
    "pwd_reset_pg_title": "비밀번호를 잊어버리셨나요?",
    "pwd_reset_pg_subtitle": "이메일 주소를 입력하면 비밀번호 재설정 지침을 보내드립니다.",
    "pwd_reset_pg_placeholder_email": "이메일 주소*",
    "pwd_reset_pg_link_login": "로그인 화면으로 돌아가기",

    #[이메일 전송 완료 페이지]
    "send_mail_pg_title": "Check Your Email",
    "send_mail_pg_subtitle": "Please check the email address hyeyoung.k111@gmail.com for instructions to reset your password.",
    
    # [회원가입 페이지]
    "signin_pg_title": "환영합니다",
    "signin_pg_subtitle": "오늘 뭐 먹지? 를 사용하시려면 회원가입을 진행해주세요.",
    "signin_pg_placeholder_email": "이메일 주소*",
    "signin_pg_placeholder_pwd": "비밀번호*",
    "signin_pg_pw_rule_title": "비밀번호는 다음을 포함해야 합니다:",
    "signin_pg_pw_rule_char_num": "At least 8 characters",
    "signin_pg_pw_rule_following": "At least 3 of the following:",
    "signin_pg_pw_rule_following_Lower_letters": "Lower case letters (a-z)",
    "signin_pg_pw_rule_following_upper_letters": "Upper case letters (A-Z)",
    "signin_pg_pw_rule_following_num": "Numbers (0-9)",
    "signin_pg_pw_rule_following_special_char": "Special characters (e.g. !@#$%^&*)",

    # [권한 요청 페이지]
    "authorize_pg_title": "Authorize App",
    "authorize_pg_email": f"Hi {dynamic_email},",
    "authorize_pg_subtitle": "Assgin-front is requesting access to your dev-aqq0w41zxvftci4m account.",
    "authorize_pg_requested_authorize": "profile: access to your profile and email",
    
    # [로그인 오류 페이지]
    "error_pg_title": "로그인 오류",
    "error_pg_subtitle": "User did not authorize the request",

    # [프로필 입력 페이지]
    "profile_pg_title": "서비스 이용을 위해 인적사항을 작성해주세요",
    "profile_pg_name_title": "이름을 입력해주세요",
    "profile_pg_name_placeholder": "이름을 입력해주세요",
    "profile_pg_team_title" : "본인이 속한 팀을 선택해주세요",
    "profile_pg_taste_title" : "음식 성향에 대해 이야기 해주세요!",

    "profile_pg_preference_title" : "추가적인 음식 성향을 이야기 해주세요!",
    "profile_pg_like_title" : "이 점은 좋아요",
    "profile_pg_dislike_title" : "이 점은 싫어요",

    "profile_pg_error_name" : "이름을 입력해주세요",
    "profile_pg_error_team" : "팀을 선택해주세요",
    "profile_pg_error_sweetness" : "맛에 대한 성향은 최소 1 이상 설정해주세요",
    "profile_pg_error_salty" : "맛에 대한 성향은 최소 1 이상 설정해주세요",
    "profile_pg_error_spicy" : "맛에 대한 성향은 최소 1 이상 설정해주세요",
    "profile_pg_error_like" : "10자 이상 입력해주세요",
    "profile_pg_error_dislike" : "10자 이상 입력해주세요",
       
    # [홈 페이지]
    "home_pg_subtitle": "직원들이 가장 선호하는 음식 종류는 무엇일까요?",

    # [히스토리 페이지]
    "history_pg_title": "추천 히스토리",
    "history_pg_subtitle": "추천 받았던 메뉴들이에요!",
    "history_pg_btn_before_review": "추천 후기 등록하기",
    "history_pg_btn_after_review": "후기 등록 완료",
}
