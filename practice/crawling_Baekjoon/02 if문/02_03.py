year = input()
year = int(year)

if year % 4 == 0:
    if year % 400 == 0 or year % 100 != 0:
        print(1)
    else:
        print(0)
    # else일때 0을 프린트해줘야한다.
else:
    print(0)
