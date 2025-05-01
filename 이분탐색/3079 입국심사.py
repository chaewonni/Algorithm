import sys
input = sys.stdin.readline

N, M = map(int, input().split())
times = list(int(input()) for _ in range(N))

start = min(times)
end = max(times) * M

answer = 0

while start <= end:
    mid = (start + end) // 2
    
    count = 0
    for t in times:
        count += mid // t
    
    if count < M:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1

print(answer)