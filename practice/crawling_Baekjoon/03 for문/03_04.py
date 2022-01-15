import sys

n = int(input())

for i in range(n):
    A, B = sys.stdin.readline().split()
    A, B = int(A), int(B)

    print(A+B)
