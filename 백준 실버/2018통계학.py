import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    nums = []

    for _ in range(N):
        nums.append(int(input()))
    
    nums.sort()

    mean = round(sum(nums) / len(nums))
    mid = nums[len(nums)//2]

    dict = {}
    for n in nums:
        dict[n] = dict.get(n, 0) + 1

    sorted_lst = sorted(dict.items(), key=lambda x: x[1], reverse=True)

    if len(sorted_lst) > 1 and sorted_lst[0][1] == sorted_lst[1][1]:
        c = sorted_lst[1][0]
    else:
        c = sorted_lst[0][0]

    # print(sorted_lst)
    
    numRange = max(nums) - min(nums) 

    print(mean)
    print(mid)
    print(c)
    print(numRange)
solve()