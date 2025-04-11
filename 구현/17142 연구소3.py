import sys
from collections import deque
input = sys.stdin.readline

# 가장 처음 모든 바이러스 비활성 상태
# 활성 상태인 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시 복제, 1초 걸림
# M개를 활성 상태로 변경하려고 함

# 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스 -> 활성 바이러스됨
# 0: 빈 칸, 1: 벽, 2: 바이러스

N, M = map(int, input().split())
lab = list(list(map(int, input().split())) for _ in range(N))

# 연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간 출력
# (바이러스 퍼뜨릴 수 없는 경우에는 -1 출력)

# 바이러스 중에 M개의 활성 바이러스를 선택하는 방법... (백트래킹?)

virus = []

# 위 아래 왼 오
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for r in range(N):
    for c in range(N):
        if lab[r][c] == 2:
            virus.append((r,c))
            
# M개 조합 만들기
result = []
def comb(idx, picked):
    if len(picked) == M:
        result.append(picked[:]) # 이거 복사 안하면 어떤 일 생기는지
        return
    if idx == len(virus):
        return
    
    # 1. 현재 인덱스 선택
    picked.append(virus[idx])
    comb(idx + 1, picked)
    picked.pop()
    
    # 2. 현재 인덱스 선택 안 함
    comb(idx + 1, picked)

comb(0, [])

empty_count = sum(row.count(0) for row in lab)

def bfs(active_virus):
    visited = [[False] * N for _ in range(N)]
    queue = deque()
    for r,c in active_virus:
        visited[r][c] = True
        queue.append((r, c, 0))
        
    infected = 0
    max_time = 0
    
    while queue:
        r, c, time = queue.popleft()
        if lab[r][c] == 0:
            infected += 1
            max_time = max(max_time, time)
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if lab[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append((nr, nc, time + 1))
                elif lab[nr][nc] == 2:
                    visited[nr][nc] = True
                    queue.append((nr, nc, time + 1))
                    
    return max_time if infected == empty_count else None
    
min_time = float('inf')    
for active_virus in result:
    res = bfs(active_virus)
    if res is not None:
        min_time = min(min_time, res)
    
print(min_time if min_time != float('inf') else -1)
    
# itertools 없이 조합을 만드는 방법 (백트래킹)을 생각했어야하는게 관건인 문제였음.