T = int(input())

max_list=[]

for i in range(T):
    lst = list(map(int, input().split()))
    for i in range(1, lst[0]+1):
        if lst[0] % i == 0:
            max_list.append(i)
    for i in range(len(max_list)):
        if lst[1] % max_list[i] == 0:
            max = max_list[i]

    min = lst[0] * lst[1] // max
    print(min)

    