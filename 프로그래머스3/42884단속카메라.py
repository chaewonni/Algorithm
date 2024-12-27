def solution(routes):
    answer = 0
    
    routes.sort(key=lambda x:x[1])
    print(routes)
    
    last_end = -30001
    
    cnt = 0
    
    for start, end in routes:
        if start > last_end:
            last_end = end
            cnt += 1
            
    return cnt