import sys
from collections import deque
input = sys.stdin.readline

A, K = map(int, input().split())

def bfs(A, K):
    queue = deque([(A, 0)])
    visited = set()
    
    while queue:
        value, count = queue.popleft()
        
        if value == K:
            return count
        
        if value + 1 <= K and value + 1 not in visited:
            visited.add(value + 1)
            queue.append((value + 1, count + 1))
            
        if value * 2 <= K and value * 2 not in visited:
            visited.add(value * 2)
            queue.append((value * 2, count + 1))
            
print(bfs(A, K))    