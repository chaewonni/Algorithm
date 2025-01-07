import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        sys.exit(0)

    land = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]

    # 상, 하, 좌, 우 + 대각선(8방향)
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]

    def dfs(r, c):
        visited[r][c] = True
        for i in range(8):
            nr = r + dy[i]
            nc = c + dx[i]
            
            if 0 <= nr < h and 0 <= nc < w:
                if land[nr][nc] == 1 and not visited[nr][nc]:
                    dfs(nr, nc)

    cnt = 0
    for i in range(h):
        for j in range(w):
            if land[i][j] == 1 and not visited[i][j]:
                cnt += 1  # 새로운 섬 발견
                dfs(i, j)

    print(cnt)
