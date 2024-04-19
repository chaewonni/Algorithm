import sys
from collections import deque

input = sys.stdin.readline

def bfs(r, c):
    if graph[r][c] == 1:
        return 0
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    queue = deque([(r,c,0)]) # (행, 열, 이동횟수)
    visited = [[False] * 5 for _ in range(5)]
    visited[r][c] = True

    while queue:
        r, c, dist = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0<=nr<5 and 0<=nc<5 and not visited[nr][nc]:
                if graph[nr][nc] == 1:
                    dist += 1
                    return dist
                elif graph[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append((nr, nc, dist+1))
    return -1

graph = []

for i in range(5):
    connection = list(map(int, input().split()))
    graph.append(connection)

    
r, c = map(int, input().split())
print(bfs(r,c))