num = input("주민등록번호: ")
inseoul = ["00", "01", "02", "03", "04", "05", "06", "07", "08"]
inbusan = ["09", "10", "11", "12"]

if num[7:9] in inseoul:
    print("서울 입니다.")
elif num[7:9] not in inseoul:
    print("서울이 아닙니다.")
