import sys
import bisect
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

# 가장 긴 증가하는 부분수열의 길이
# 6
# 10 20 10 30 20 50
lis = [0]

for n in nums:
    if n > lis[-1]:
        lis.append(n)
    else:
        idx = bisect.bisect_left(lis, n)
        lis[idx] = n

print(len(lis)-1)