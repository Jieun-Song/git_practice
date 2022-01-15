a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print((a+b) % c)
print(((a % c)+(b % c)) % c)
print((a*b) % c)
print(((a%c)*(b % c)) % c)

# 예제대로 답도 나오는데 왜 실패라고 뜰까, , ?
