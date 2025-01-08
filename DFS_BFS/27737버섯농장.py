import sys
import math
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())

farm = []
zero = False # 0칸이 존재하는지 확인!
result = 0

for _ in range(N):
    row = list(map(int, input().split()))
    farm.append(row)

    if 0 in row:
        zero = True
        
if not zero:
    print('IMPOSSIBLE')
    sys.exit(0)
    
# 상 하 좌 우
dx = [0, 0, -1 , 1]
dy = [-1, 1, 0, 0]

def bfs(r,c):
    global result
    global cnt
    queue = deque([(r,c)])
    
    farm[r][c] = 1
    
    while queue:
        r,c = queue.popleft()
        
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            
            if 0 <= nr < N and 0 <= nc < len(farm[0]):
                if farm[nr][nc] == 0:
                    cnt += 1
                    queue.append((nr, nc))
                    farm[nr][nc] = 1
                                  
    result += math.ceil(cnt / K)
    
for i in range(N):
    for j in range(len(farm[0])):
        if farm[i][j] == 0:
            cnt = 1
            bfs(i,j)
            
if result > M:
    print('IMPOSSIBLE')
else:
    print('POSSIBLE')
    print(M-result)
    
