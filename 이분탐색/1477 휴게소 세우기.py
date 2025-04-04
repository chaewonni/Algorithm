import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
road = list(map(int, input().split()))
road.append(0)
road.append(L)
road.sort()

gaps = []

for i in range(len(road)-1):
    gaps.append(road[i+1] - road[i])

start = 1
end = L

result = 0

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    
    for gap in gaps:
        cnt += (gap - 1) // mid
        
    if cnt > M: # 휴게소 M개 필요한데 cnt가 더 많을 때 (즉 구간이 더 좁을 때 = 구간 늘려야함)
        # cnt가 더 크다는 건 cnt만큼 휴게소가 더 필요한 상황
        start = mid + 1
    else: # 휴게소 M 개 필요한데 cnt가 같거나 적을 때 (구간 줄여야함)
        # 휴게소 덜 필요해
        result = mid
        end = mid - 1
        
print(result)