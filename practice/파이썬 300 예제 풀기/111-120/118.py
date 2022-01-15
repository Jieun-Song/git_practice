warn_investment_list = ["Microsoft", "Google",
                        "Naver", "Kakao", "SAMSUNG", "LG"]

investment_name = input("종목명을 입력하십시오:")

if investment_name in warn_investment_list:
    print("투자 경고 종목입니다.")
elif not investment_name in warn_investment_list:
    print("투자 경고 종목이 아닙니다.")
