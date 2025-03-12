import sys
import copy
input = sys.stdin.readline

R, C = map(int, input().split())

maps = [list(input().strip()) for _ in range(R)]
sink = copy.deepcopy(maps)

# 위 아래 왼 오
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for r in range(R):
    for c in range(C):
        if maps[r][c] == 'X':
            cnt = 0
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
            
                if 0 <= nr < R and 0 <= nc < C:
                    if maps[nr][nc] == '.':
                        cnt += 1
                else:
                    cnt += 1
                    
            if cnt >= 3:
                sink[r][c] = '.'

min_row, max_row = R, 0
min_col, max_col = C, 0

for r in range(R):
    for c in range(C):
        if sink[r][c] == 'X':
            min_row = min(min_row, r)
            max_row = max(max_row, r)
            min_col = min(min_col, c)
            max_col = max(max_col, c)


for r in range(min_row, max_row + 1):
    print(''.join(sink[r][min_col:max_col+1]))
    