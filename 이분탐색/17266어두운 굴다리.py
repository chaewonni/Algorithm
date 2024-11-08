import sys
import math
input = sys.stdin.readline

N = int(input())
M = int(input())
location = list(map(int, input().split()))

start = 0
end = N

n_list = []

for i in range(len(location) - 1, 0, -1):
    n_list.append(math.ceil((location[i] - location[i-1]) / 2))

n_list.append(end - location[M-1])
n_list.append(location[0]- start)

print(max(n_list))