import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 놀이기구 비어있으면 현재 줄에서 가장 앞에 서 있는 아이가 빈 놀이기구에 탑승 
# 여러 개의 놀이기구가 동시에 비어있으면, 더 작은 번호가 적혀 있는 놀이기구 먼저 탑승

# 줄의 마지막 아이가 타게 되는 놀이기구의 번호

if N <= M:
    print(N)
    sys.exit()

def cal_time(time):
    count = M
    for a in arr:
        count += time // a
    return count

low = 1
high = N * 30
answer = 0

while low <= high:
    mid = (low + high) // 2

    # 시간이 부족, 시간을 더 늘려야함
    if cal_time(mid) < N:
        low = mid + 1
    else:
        answer = mid
        high = mid - 1

# answer = 최소시간
count = cal_time(answer - 1)

for idx, a in enumerate(arr):
    if answer % a == 0:
        count += 1
    if count == N:
        print(idx+1)
        break