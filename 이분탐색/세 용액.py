import sys
input = sys.stdin.readline

# 같은 양의 세가지 용액 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합
# 세가지 용액 혼합하여 특성값이 0에 가까운 용액 만들기

liquid = float('inf')

N = int(input())
nums = list(map(int, input().split()))

nums.sort()

for i in range(N-2):
    for j in range(i+1, N-1):
        first = nums[i]
        second = nums[j]

        start = j + 1
        end = N - 1

        while start <= end:
            mid = (start + end) // 2

            now_liquid = first + second + nums[mid]
            if abs(now_liquid) < liquid:
                liquid = abs(now_liquid)
                x = first
                y = second
                z = nums[mid]

            if now_liquid < 0:
                start = mid + 1
            else:
                end = mid - 1

print(x, y, z)

# 특성값이 0에 가장 가까운 용액 만들어내는 세 용액의 특성값 출력 (오름차순)