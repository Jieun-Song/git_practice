H, M = input().split()
H = int(H)
M = int(M)

if M < 45:
    H -= 1
    M += 15
    if H < 0:
        H += 24
else:
    M -= 45

print(H, M)

# 꼭 else도 쓸것
