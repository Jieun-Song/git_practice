money = input("입력: ")

money = money.split(" ")

if money[1] == "달러":
    print(float(money[0])*1167, "원")
if money[1] == "엔":
    print(float(money[0])*1.096, "원")
if money[1] == "유로":
    print(float(money[0])*1268, "원")
if money[1] == "위안":
    print(float(money[0])*171, "원")
