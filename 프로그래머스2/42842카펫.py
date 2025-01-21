def solution(brown, yellow):
    answer = []
    num = brown // 2
    cnt = 1
    
    a = num - cnt
    b = cnt
    while a - b > 1:
        
        if (a-2) * b == yellow:
            return [a, b+2]
        
        a -= 1
        b += 1
    return answer