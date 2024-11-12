import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
A,B = map(int, input().split())
m = int(input())

g = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a,b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

def bfs(g, n, visited):
    visited[n] = True
    queue = deque([[n, 0]])

    while queue:
        num, depth = queue.popleft()
        if num == B:
            return depth
        for i in g[num]:
            if not visited[i]:
                queue.append([i, depth+1])
                visited[i] = True

    return -1


result = bfs(g, A, visited)

print(result)