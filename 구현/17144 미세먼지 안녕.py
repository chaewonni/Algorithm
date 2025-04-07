import sys
import copy
import math
input = sys.stdin.readline

# 공기청정기 항상 1번열, 크기 두 행
# 1. 확산
# 인접한 네 방향으로, 인접한 방향에 공기청정기 있거나 칸 없으면 확산 X
# 인접한 곳에 확산되는 양 floor(A r,c / 5)
# (r, c)에 남은 미세먼지의 양은 Ar,c - ⌊Ar,c/5⌋×(확산된 방향의 개수) 

# 2. 공기청정기 작동
# 바람 나옴
# 위쪽 공기청정기 바람은 반시계 방향, 아래쪽 공기청정기 바람은 시계 방향
# 바람 불면 미세먼지가 바람 방향대로 모두 한 칸씩 이동
# 공기 청정기에서 부는 바람: 미세먼지 x, 공기 청정기로 들어간 미세먼지: 모두 정화됨

# 행, 열, T 초가 지난 후 미세먼지 양
R, C, T = map(int, input().split())
# 공기청정기 설치된 곳 -1, 나머지 미세먼지 양
room = list(list(map(int, input().split())) for _ in range(R))

# 위 아래 왼 오
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

air_cleaner = []
for r in range(R):
    if room[r][0] == -1:
        air_cleaner.append(r)

top = air_cleaner[0] # 위쪽 공기청정기 행
bottom = air_cleaner[1] # 아래쪽 공기청정기 행

for _ in range(T):
    room_copy = copy.deepcopy(room)
    # 미세먼지 확산
    for r in range(R):
        for c in range(C):
            if room[r][c] != -1:
                cnt = 0
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    
                    if 0 <= nr < R and 0 <= nc < C and room[nr][nc] != -1:
                        room_copy[nr][nc] += math.floor(room[r][c] / 5)
                        cnt += 1
                        
                room_copy[r][c] = room_copy[r][c] - math.floor(room[r][c] / 5) * cnt
                
    room = room_copy
                
    # 미세먼지 순환
    # 위쪽 반시계, 아래쪽 시계 방향
    # 현재 행이 공기청정기 행(top)보다 위면 반시계

    # 0열은 밑으로, 근데 공기청정기 top과 같은 행은 사라짐
    for r in range(top-1, 0, -1):
        room[r][0] = room[r-1][0]
    # 0행
    for c in range(0, C-1):
        room[0][c] = room[0][c+1]
    # C열은 위로, 근데 0행은 왼쪽
    for r in range(0, top):
        room[r][C-1] = room[r+1][C-1]
    # top 행
    for c in range(C-1, 1, -1):
        room[top][c] = room[top][c-1]
    
    room[top][1] = 0
        
    # 현재 행이 공기청정기 행(bottom)보다 아래면 시계
    # 0 열
    for r in range(bottom+1, R-1):
        room[r][0] = room[r+1][0]
    # 맨 마지막 행
    for c in range(0, C-1):
        room[R-1][c] = room[R-1][c+1]
    # 맨 오른쪽 열
    for r in range(R-1, bottom, -1):
        room[r][C-1] = room[r-1][C-1]
    # bottom 행
    for c in range(C-1, 1, -1):
        room[bottom][c] = room[bottom][c-1]
    
    room[bottom][1] = 0

    
total = 0
for r in range(R):
    for c in range(C):
        if room[r][c] != -1:
            total += room[r][c]

print(total)
# 순환은 행단위, 열단위이기 떄문에 좌표 하나하나 하는 것보다
# 행단위, 열단위로 생각해서 했어야 했다