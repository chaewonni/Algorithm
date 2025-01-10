import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
rgb = []

for _ in range(N):
    rgb.append(list(input().strip()))  # 문자열 그대로 저장

# 적록색약
rb = [['R' if color == 'G' else color for color in row] for row in rgb]

# 방향 벡터 (상, 하, 좌, 우)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(r, c, visited, grid):
    queue = deque([(r, c)])
    visited[r][c] = True
    color = grid[r][c]
    
    while queue:
        r, c = queue.popleft()
        
        for k in range(4):
            nr = r + dx[k]
            nc = c + dy[k]
            
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and grid[nr][nc] == color:
                visited[nr][nc] = True
                queue.append((nr, nc))

def count(grid):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                cnt += 1
                bfs(i, j, visited, grid)
                
    return cnt 

normal_cnt = count(rgb)
not_normal_cnt = count(rb)

print(normal_cnt, not_normal_cnt)
