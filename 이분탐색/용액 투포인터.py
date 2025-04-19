import sys
input = sys.stdin.readline

liquid = float('inf')
N = int(input())
nums = list(map(int, input().split()))

left_pointer =  0
right_pointer = N-1

while left_pointer < right_pointer:
    now = nums[left_pointer] + nums[right_pointer]

    if abs(now) < liquid:
        x = nums[left_pointer]
        y = nums[right_pointer]
        liquid = abs(now)

    if now < 0:
        left_pointer += 1
    else:
        right_pointer -= 1

print(x,y)