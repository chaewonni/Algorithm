import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

R, C = map(int, input().split())

# 위 아래 오른쪽 왼쪽
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
    
map = list(list(input().strip()) for _ in range(R))

def dfs(r,c,prev_r, prev_c):
    visited[r][c] = True
    
    f_cnt, s_cnt = 0, 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        
        if 0 <= nr < R and 0 <= nc < C and map[nr][nc] == '.':
            f_cnt += 1
            if visited[nr][nc]:
                if nr == prev_r and nc == prev_c:
                    s_cnt += 1
            else:
                dfs(nr, nc, r, c)
        
    if f_cnt == s_cnt:
        print(1)
        sys.exit()
            

for r in range(R):
    for c in range(C):
        if map[r][c] == '.':
            visited = [[False] * C for _ in range(R)]
            dfs(r,c,-1,-1)
            
print(0)