address_num = input("우편번호: ")

if address_num[0] == "0" and address_num[1] == "1":
    if address_num[2] in "012":
        print("강북구")
    elif address_num[2] in "345":
        print("도봉구")
    elif address_num[2] in "6789":
        print("노원구")
