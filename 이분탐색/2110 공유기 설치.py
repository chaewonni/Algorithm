import sys
input = sys.stdin.readline

N, C = map(int, input().split())
router = []
for _ in range(N):
    router.append(int(input().strip()))

router.sort()

# 5 3
# 1 2 4 8 9
# 가장 인접한 두 공유기 사이의 거리 최대 
# -> 가장 인접하지 않은 애들도 인접하지 않은 거 생각해야하잖아
# 생각을 바꿔서... 
# mid를 가장 인접한 차이라고 생각하고 줄여나가거나 늘려나가자
# 1, 8

start = 1
end = router[N-1] - router[0]
answer = 0

while start <= end:
    mid = (start + end) // 2

    cnt = 1
    last = router[0]
    for i in range(1, N):
        if router[i] - last >= mid:
            last = router[i]
            cnt += 1

    if cnt >= C:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)