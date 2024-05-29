import sys
input = sys.stdin.readline

N = int(input())
K = list(map(int, input().split()))
M = int(input())
start, end = 0, max(K) # 0 150

#이분탐색
while start <= end:
    mid = (start + end) // 2 # 75, 113
    total = 0
    for i in K:
        if i > mid: 
            total += mid 
        else:
            total += i

    if total <= M:
        start = mid + 1 # 76
    else: 
        end = mid - 1

print(end)