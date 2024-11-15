def solution(nums):
    answer = 0
    dict = {}
    
    n = len(nums)
    
    for num in nums:
        dict[num] = dict.get(num,0) + 1
        
    if len(dict) >= n//2:
        answer = n//2
    else:
        answer = len(dict)
    return answer