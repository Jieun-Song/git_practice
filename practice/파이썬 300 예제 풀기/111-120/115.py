a = int(input("입력값:"))

if a - 20 < 0:
    print("출력값: 0")
elif 0 < a - 20 < 255:
    print("출력값:", a - 20)
elif 255 < a - 20:
    print("출력값: 255")
