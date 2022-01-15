cycle = 0
a = int(input())
if a < 10:
    one_a = a
    new_a = a*10 + one_a
else:
    one_a = a%10
    new_a = (a//10) + (a%10)

if new_a != a:
    while cycle<30:
        print(new_a)
        if new_a < 10:
            new_a = new_a*10 + one_a
        elif a==new_a:
            print(cycle)
            break
        else:
            new_a = new_a//10 + one_a
        one_a = (new_a%10)
        cycle += 1
else:
    print("1")