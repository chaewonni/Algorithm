import sys

n=1000001
array=[True]*n

for i in range(2, int(n ** 0.5)+1):
    if array[i]:
        for j in range(i*2, n, i):
            array[j] = False

N = int(sys.stdin.readline())

for i in range(N, n):
    num=int(''.join(reversed(str(i))))
    if i == 1:
        continue
    if i == 1000000:
        i = 1003001
        break
    if array[i] and i == num:
        break
    else:
        continue

print(i)