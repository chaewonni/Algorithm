import sys
from collections import deque
input = sys.stdin.readline

W, H = map(int, input().split())
maps = [list(input().strip()) for _ in range(H)]

print()

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

laser = []
visited = [[False] * W for _ in range(H)]

for r in range(H):
    for c in range(W):
        if maps[r][c] == 'C':
            laser.append((r,c))

flr, flc = laser[0]
slr, slc = laser[1]

INF = 10**9
# dist[r][c][k]: (r,c)에 방향 k 로 도달했을 때 거울 최소 개수
dist = [[[INF]*4 for _ in range(W)] for _ in range(H)]
dq = deque()

for k in range(4):
    dist[flr][flc][k] = 0
    dq.append((flr, flc, k))

while dq:
    r, c, prev = dq.popleft()
    cur = dist[r][c][prev]

    for k in range(4):
        nr, nc = r, c

        while True:
            nr += dr[k]
            nc += dc[k]
            
            if not (0 <= nr < H and 0 <= nc < W):  # 경계 벗어나면 중단
                break
            if maps[nr][nc] == '*':               # 벽 만나면 중단
                break

            next_cost = cur + (0 if k == prev else 1)

            if next_cost < dist[nr][nc][k]:
                dist[nr][nc][k] = next_cost
                if k == prev:
                    dq.appendleft((nr, nc, k))
                else:
                    dq.append((nr, nc, k))

print(min(dist[slr][slc]))