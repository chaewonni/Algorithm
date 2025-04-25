import sys
input = sys.stdin.readline

# 같은 양의 세가지 용액 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합
# 세가지 용액 혼합하여 특성값이 0에 가까운 용액 만들기

liquid = float('inf')

N = int(input())
nums = list(map(int, input().split()))

nums.sort()

for i in range(N-2):
    left_pointer = i+1
    right_pointer = N-1

    # 투 포인터
    while left_pointer < right_pointer:

        now = nums[i] + nums[left_pointer] + nums[right_pointer]

        if abs(now) < liquid:
            x = nums[i]
            y = nums[left_pointer]
            z = nums[right_pointer]

            liquid = abs(now)

        if now < 0:
            left_pointer += 1
        else:
            right_pointer -= 1

print(x, y, z)