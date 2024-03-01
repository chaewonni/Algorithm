import sys
import copy

R, C = map(int, sys.stdin.readline().split())
e_map = []

for i in range(R):
    e_map.append(list(sys.stdin.readline().strip()))

sink = copy.deepcopy(e_map)

# 상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for y in range(R):
    for x in range(C):
        cnt = 0
        if e_map[y][x] == 'X':
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < C and 0 <= ny < R:
                    if e_map[ny][nx] == '.':
                        cnt += 1
                else:
                    cnt += 1
            if cnt >= 3:
                sink[y][x] = '.'

# 50년 후 지도 출력하기
min_x, max_x = C-1, 0
min_y, max_y = R-1, 0

for y in range(R):
    for x in range(C):
        if 'X' in sink[y][x]:
            min_x = min(x, min_x)
            max_x = max(x, max_x)
            min_y = min(y, min_y)
            max_y = max(y, max_y)

for y in range(min_y, max_y + 1):
    print("".join(sink[y][min_x:max_x+1]))