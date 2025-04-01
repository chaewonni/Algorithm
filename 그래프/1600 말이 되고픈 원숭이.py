import sys
from collections import deque
input = sys.stdin.readline

K = int(input())
W, H = map(int, input().split())

grid = list(list(map(int, input().split())) for _ in range(H))

# 위 아래 왼 오
horse_moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),(2, 1), (1, 2), (-1, 2), (-2, 1)]
normal_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(r, c):
    visited = [[[False] * (K+1) for _ in range(W)] for _ in range(H)]
    queue = deque([(r, c, 0, 0)]) # r, c, 말 이동 횟수, 이동 횟수
    visited[r][c][0] = True
    
    while queue:
        r, c, horse_cnt, move_cnt = queue.popleft()
        
        # 끝에 도착했을 때
        if r == H-1 and c == W-1:
            print(move_cnt)
            return 
        
        # 말 이동은 선택지! 무조건 해야하는 건 아님
        for dr, dc in normal_moves:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc][horse_cnt] and grid[nr][nc] == 0:
                visited[nr][nc][horse_cnt] = True
                queue.append((nr, nc, horse_cnt, move_cnt + 1))
                
        if horse_cnt < K:
            for dr, dc in horse_moves:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc][horse_cnt + 1] and grid[nr][nc] == 0:
                    visited[nr][nc][horse_cnt + 1] = True
                    queue.append((nr, nc, horse_cnt + 1, move_cnt + 1))
        
    print(-1)
            
bfs(0, 0)