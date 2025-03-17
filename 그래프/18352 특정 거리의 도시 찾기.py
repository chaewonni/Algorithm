import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    arr[A].append(B)

result = []

def bfs(num):
    queue = deque([(num,0)])
    visited[num] = True
    
    while queue:
        num, cnt = queue.popleft()
        
        if cnt == K:
            result.append(num)
            
        for node in arr[num]:
            if not visited[node]:
                queue.append((node, cnt + 1))
                visited[node] = True  
  
bfs(X)

if result:
    result.sort()
    for i in result:
        print(i)
else:
    print(-1)