# n은 입력값으로 자연수로 입력받는다.
# n차원으로 구성되며 각 차원의 배열의 길이가 n인 배열을 만드시오
# 단 초기의 배열값은 0임.
# from copy import deepcopy로 deepcopy()를 사용할 수 있음

n = input("자연수 입력")
list = []

for i in n:
    # 몇차원인지

    for m in n:
        m = []
        m.append(0)
        list.append(m)

print(list)

#지은아 잘부탁한다. 못풀었다.
#미래의 너는 플수 있겠지...
#기대하겠다...
