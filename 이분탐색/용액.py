import sys
input = sys.stdin.readline

liquid = float('inf')
N = int(input())
nums = list(map(int, input().split()))

for i in range(N-1):
    now = nums[i]

    start = i + 1
    end = N - 1

    while start <= end:
        mid = (start + end) // 2
        now_liquid = now + nums[mid]

        if abs(now_liquid) < liquid:
            liquid = abs(now_liquid)
            x = now
            y = nums[mid]

        if now_liquid < 0:
            start = mid + 1
        else:
            end = mid - 1

print(x, y)

# 이분탐색은 무조건 숫자 아니고 인덱스로도 가능하다........