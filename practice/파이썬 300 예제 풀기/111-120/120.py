fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
i = input("좋아하는과일은?")

if i in fruit.values():
    print("정답입니다.")
elif not i in fruit.values():
    print("오답입니다.")
