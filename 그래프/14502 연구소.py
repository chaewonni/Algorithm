import sys
import copy
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

virus = []

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for r in range(N):
    for c in range(M):
        if maps[r][c] == 2:
            virus.append((r,c))

result = []

def spread(maps):
    queue = deque()
    visited = [[False] * M for _ in range(N)]
    for r,c in virus:
        queue.append((r,c))
        visited[r][c] = True

    while queue:
        r, c = queue.popleft()

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if maps[nr][nc] == 0:
                    maps[nr][nc] = 2
                    queue.append((nr, nc))

empty = [(r, c) for r in range(N) for c in range(M) if maps[r][c] == 0]

def backtracking(depth, start):
    global result

    if depth == 3:
        cnt = 0
        tmp = copy.deepcopy(maps)
        spread(tmp)
        for r in range(N):
            for c in range(M):
                if tmp[r][c] == 0:
                    cnt += 1
        
        result.append(cnt)
        return

    for i in range(start, len(empty)):
        r,c = empty[i]
        maps[r][c] = 1
        backtracking(depth + 1, i + 1)
        maps[r][c] = 0

backtracking(0, 0)
print(max(result))