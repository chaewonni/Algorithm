def solution(citations):
    answer = 0
    
    # 설정 잘해줘야지
    start, end = 0, len(citations)
    
    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        
        for c in citations:
            if c >= mid:
                cnt += 1
                
        if cnt >= mid:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
        
    return answer