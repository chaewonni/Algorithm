import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0

def dfs(index, total):
    global cnt
    
    if index == N:
        return
    
    total += arr[index]
    if total == S:
        cnt += 1
        
    # 현재 원소 선택
    dfs(index + 1, total)
    
    # 현재 원소 선택 안함
    dfs(index + 1, total-arr[index])  
    
dfs(0, 0)

print(cnt)