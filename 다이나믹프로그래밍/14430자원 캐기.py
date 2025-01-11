import sys
input = sys.stdin.readline

N, M = map(int, input().split())

area = [list(map(int, input().split())) for _ in range(N)]

# 왼쪽, 위
dr = [0, -1]
dc = [-1, 0]

for r in range(N):
    for c in range(M):
        max_num = 0
        
        for k in range(2):
            nr = r + dr[k]
            nc = c + dc[k]
            
            if 0 <= nr < N and 0 <= nc < M:
                max_num = max(max_num, area[nr][nc])
                
        area[r][c] += max_num          

print(area[N-1][M-1])