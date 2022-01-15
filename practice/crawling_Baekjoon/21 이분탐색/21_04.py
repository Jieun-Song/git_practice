n, m = input().split()
n, m = int(n), int(m)

trees = list(map(int,input().split()))

h = int(max(trees))
while 1:

    plus = 0


    for i in trees:
        if int(i)-h>0:
            plus+=int(i)-h
        else:
            plus+=0
    print(plus)
    if plus < m:
        print(h)
        h/2
    elif plus > m:
        print(h)
    else:
        break
    