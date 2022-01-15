cycle = 0
x1 = int(input())

if 0 <= x1 < 10:
    x1 = x1 * 10

while 1:
    print("1")
    x2 = x1 % 10 + x1 // 10

    if x1 == x2:
        break
    else:
        x2 = (x1 % 10) * 10 + x2 % 10
        cycle += 1

print(cycle)