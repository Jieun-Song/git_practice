num = input("주민등록번호: ")
result = 0

for i in range(13):
    if i == 6:
        pass
    elif i <= 7:
        print(int(num[i]) * (i+2))
        result += int(num[i]) * (i+2)

    elif 8 <= i:
        print(int(num[i]) * (i-7))
        result += int(num[i]) * (i-7)

print(result)
if num[13] == 11 - result % 11:
    print("유효한 주민등록번호입니다.")

elif num[13] != 11 - result % 11:
    print("유효하지않은 주민등록번호입니다.")
