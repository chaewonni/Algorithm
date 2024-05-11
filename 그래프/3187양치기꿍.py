import sys
from collections import deque

input = sys.stdin.readline

def bfs(r,c):

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    queue.append([r,c])
    visited[r][c] = True

    v_cnt = 0
    k_cnt = 0

    while queue:
        r,c = queue.popleft()

        if graph[r][c] == 'v':
            v_cnt += 1
        elif graph[r][c] == 'k':
            k_cnt += 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < M and 0 <= nc < N:
                if graph[nr][nc] != '#' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append([nr,nc])

    if v_cnt >= k_cnt:
        k_cnt = 0
    else:
        v_cnt = 0

    return [v_cnt, k_cnt]


M,N = map(int, input().split())
graph = [list(input().strip()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]
queue = deque()

v, k = 0,0
for i in range(M):
    for j in range(N):
        if graph[i][j] != '#' and not visited[i][j]:
            v_cnt, k_cnt = bfs(i, j)
            v += v_cnt
            k += k_cnt

print(k, v)

