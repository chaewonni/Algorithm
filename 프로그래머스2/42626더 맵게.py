import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    cnt = 0
    
    for s in scoville:
        heapq.heappush(heap, s)
        
    while heap[0] < K:
        if len(heap) < 2:
            cnt = -1
            break
        cnt += 1
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        
        new = a + 2*b
        
        heapq.heappush(heap, new)
        
    return cnt