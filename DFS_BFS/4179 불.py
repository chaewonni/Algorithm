import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
miro = []
fire_list = []
for i in range(R):
    miro.append(list(input().strip()))
    for j in range(len(miro[i])):
        if miro[i][j] == 'J':
            sr, sc = i, j
        if miro[i][j] == 'F':
            fire_list.append((i,j))

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[False] * C for _ in range(R)]
fire_visited = [[-1] * C for _ in range(R)]

# 불 먼저 퍼뜨리기
# 불은 각 지점에서 네 방향으로 확산
def spread_fire():
    queue = deque()
    for fr, fc in fire_list:
        fire_visited[fr][fc] = 0
        queue.append((fr, fc))

    while queue:
        r, c = queue.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                if miro[nr][nc] != '#' and fire_visited[nr][nc] == -1:
                    fire_visited[nr][nc] = fire_visited[r][c] + 1
                    queue.append((nr, nc))

def bfs(sr, sc):
    queue = deque([(sr, sc, 0)])
    visited[sr][sc] = True

    while queue:
        r, c, cnt = queue.popleft()

        if (r == 0 or r == R-1) or (c == 0 or c == C-1):
            return cnt + 1

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < R and 0 <= nc < C and miro[nr][nc] != '#' and miro[nr][nc] != 'F':
                if visited[nr][nc]:
                    continue
                if miro[nr][nc] == '#':
                    continue
                if fire_visited[nr][nc] != -1 and fire_visited[nr][nc] <= cnt + 1:
                    continue

                visited[nr][nc] = True
                queue.append((nr, nc, cnt + 1))
    
    return 'IMPOSSIBLE'

spread_fire()
result = bfs(sr, sc)
print(result)