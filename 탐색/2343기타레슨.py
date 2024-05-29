import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 9개 강의, 3개의 블루레이
course = list(map(int, input().split()))

start = max(course) # 9 (가능한 블루레이 크기 중 가장 작은 값)
end = sum(course)   # 45 (가능한 블루레이 크기 중 가장 큰 값)

while start <= end:
    mid = (start + end) // 2 # 27

    total = 0
    cnt = 1
    for i in course:
        if total + i > mid:
            cnt += 1
            total = 0
        
        total += i

    if cnt <= M:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)