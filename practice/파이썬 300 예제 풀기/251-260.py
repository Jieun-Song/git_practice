# 251

#클래스: 설계도면
#객체: 차
# 인스턴스:설계도면으로 만들어지는 차

# 252

# class Human:
#     pass

# 253

# class Human():
#     pass

# areum = Human()

# 254

# class Human():
#     print("응애응애")

# Human()

# 255

# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.name = age
#         self.sex = sex


# areum = Human("아름", 25, "여자")

# 256

# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex


# areum = Human("아름", 25, "여자")
# print(areum.name, areum.age, areum.sex)

# 257


# class Human:
#     def setInfo(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex


# areum = Human("아름", 25, "여자")
# print(areum.name, areum.age, areum.sex)

# 258

class Human():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


areum = Human("모름", 0, "모름")
areum.setInfo("아름", 25, "여자")

# 259

# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

#     def __del__(self):
#         print("나의 죽음을 알리지 마라")


# areum = Human("아름", 25, "여자")
# del areum

# 260

# self가 없어서
