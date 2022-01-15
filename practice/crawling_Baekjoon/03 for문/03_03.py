import sys
input = sys.stdin.readline
n = input()
n = int(n)
sum = 0
for i in range(n):
    sum += i + 1
print(sum)
