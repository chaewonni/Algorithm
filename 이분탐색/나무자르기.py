import sys
input = sys.stdin.readline

N, M = map(int, input().split())
length = list(map(int, input().split()))

start = 0
end = max(length)

result = 0

while start <= end:
    
    mid = (start + end) // 2
    
    cut = sum(namu - mid for namu in length if namu > mid)
        
    if cut >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(result)