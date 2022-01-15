# 221

# def print_reverse(i):
#     a = ""
#     for j in i[::-1]:
#         a += j
#     print(a)


# print_reverse("phython")

# 222

# def print_score(score_list):
#     a = 0
#     for i in score_list:
#         a += i
#     print(a/len(score_list))


# print_score([1, 2, 3])

# 223

# def print_even(list):
#     result = []
#     for i in list:
#         if i % 2 == 0:
#             result.append(i)
#     print(result)


# print_even([1, 3, 2, 10, 12, 11, 15])

# 224

# def print_keys(dic):
#     for i in dic.keys():
#         print(i)

# print_keys({"이름": "김말똥", "나이": 30, "성별": 0})

# 225

# def print_value_by_key(list, date):
#     print(list[date])


# my_dict = {"10/26": [100, 130, 100, 100],
#            "10/27": [10, 12, 10, 11]}

# print_value_by_key(my_dict, "10/26")

# 226
# def print_5xn(text):
#     a = ""
#     for i in range(len(text)//5+1):
#         print(text[0+5*i:5+5*i])


# print_5xn("아이엠어보이유알어걸")

# 227

# def printmxn(text, count):
#     a = ""
#     for i in range(len(text)//count+1):
#         print(text[0+count*i:count+count*i])


# printmxn("아이엠어보이유알어걸", 3)

# 228

# def calc_monthly_salary(annual_salary):
#     print(annual_salary//12)

# calc_monthly_salary(12000000)

# 229

# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)

# my_print(a=100, b=200)

# 왼쪽 100
# 오른쪽 200

# 230

# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)

# my_print(b=100, a=200)

#왼쪽: 200
#오른쪽: 100
