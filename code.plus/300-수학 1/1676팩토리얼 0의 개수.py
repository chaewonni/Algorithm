N=int(input())

num = 1

lst = []

for i in reversed(range(1, N+1)):
    num = num * i

num = str(num)

for i in num:
    lst.append(i)

lst.reverse()

cnt = 0

for i in range(len(lst)):
    if lst[i] == '0':
        cnt += 1
    else:
        break

print(cnt)