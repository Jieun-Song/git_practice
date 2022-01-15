import sys
n = int(input())

for i in range(n):
    A, B = sys.stdin.readline().split()
    A, B = int(A), int(B)
    i = str(i+1)
    print("Case #"+i+":", A, "+", B, "=", A+B)
