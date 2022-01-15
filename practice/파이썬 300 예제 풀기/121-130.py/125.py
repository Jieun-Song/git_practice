p_number = input("휴대전화 번호 입력: ")
p_number = p_number.split("-")
if p_number[0] == "011":
    print("당신은 SKT 사용자 입니다.")
elif p_number[0] == "016":
    print("당신은 KT 사용자 입니다.")
elif p_number[0] == "019":
    print("당신은 LGU 사용자 입니다.")
elif p_number[0] == "010":
    print("알수 없습니다.")
