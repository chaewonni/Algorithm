N=int(input())

num = 1

for i in reversed(range(1, N+1)):
    num = num * i

print(num)