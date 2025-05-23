from collections import deque
import sys
input = sys.stdin.readline

# 두 나라의 인구 차이 L명 이상, R명 이하 -> 하루 동안 국경선 열음 (얘네 연합)
# 국경선 모두 열렸다면, 인구 이동 시작
# 연합을 이루고 있는 각 칸의 인구 수 : (연합의 인구수) / (연합을 이루고 있는 칸의 개수) (소수점 버림)
# 연합 해체하고, 국경선 닫음

# 50 30 30 40

N, L, R = map(int, input().split()) # 땅 크기, L명 이상 R명 이하 (2, 20 50)
country = [list(map(int, input().split())) for _ in range(N)]

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(i, j, visited):
    queue = deque([(i,j)])
    visited[i][j] = True
    union = [(i,j)] # 연합
    total = country[i][j]

    while queue:
        r, c = queue.popleft()
        
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if L <= abs(country[r][c] - country[nr][nc]) <= R:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    union.append((nr, nc))
                    total += country[nr][nc]

    if len(union) > 1:
        new_pop = total // len(union)
        for r, c in union:
            country[r][c] = new_pop
        return True
    
    return False

day = 0
while True:
    visited = [[False] * N for _ in range(N)]
    moved = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j, visited):
                    moved = True


    if not moved:
        print(day)
        sys.exit()
    else:
        day += 1