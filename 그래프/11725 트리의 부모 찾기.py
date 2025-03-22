import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N+1)]

new_arr = [0] * (N+1) 
visited = [False] * (N+1)

# 인접리스트
for _ in range(N-1):
    A, B = map(int, input().split())
    arr[A].append(B)
    arr[B].append(A)

    
def bfs(num):
    queue = deque([num])
    visited[num] = True
    
    while queue:
        num = queue.popleft()
        
        for node in arr[num]:
            if not visited[node]:
                queue.append(node)
                new_arr[node] = num
                visited[node] = True  
    
bfs(1)

for i in range(2, N+1):
    print(new_arr[i])