import sys
import copy

# 입력받은 지도의 행(R)과 열(C) 크기를 정수로 변환
R, C = map(int, sys.stdin.readline().split())
e_map = []  # 초기 지도 상태를 저장할 리스트

# 입력받은 지도 정보를 행별로 읽어서 e_map에 저장
for i in range(R):
    e_map.append(list(sys.stdin.readline().strip()))

# e_map을 복사하여 50년 후의 지도 상태를 예측할 sink 리스트 생성
sink = copy.deepcopy(e_map)

# 상하좌우 이동을 위한 dx, dy 정의
dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 지도의 모든 위치에 대해 검사
for y in range(R):
    for x in range(C):
        cnt = 0  # 주변 바다('.‘)의 개수를 세기 위한 카운터
        if e_map[y][x] == 'X':  # 현재 위치가 땅('X')인 경우
            for i in range(4):  # 상하좌우 네 방향에 대해 검사
                nx = x + dx[i]  # 다음 위치의 x 좌표
                ny = y + dy[i]  # 다음 위치의 y 좌표
                # 다음 위치가 지도 범위 내에 있고 바다('.')인 경우 cnt 증가
                if 0 <= nx < C and 0 <= ny < R:
                    if e_map[ny][nx] == '.':
                        cnt += 1
                else:  # 다음 위치가 지도 범위 밖인 경우(바다로 간주) cnt 증가
                    cnt += 1
            # 주변 바다의 개수가 3개 이상인 경우 50년 후에는 바다('.')가 됨
            if cnt >= 3:
                sink[y][x] = '.'

# 50년 후 지도의 출력 범위를 찾기 위한 변수 초기화
min_x, max_x = C-1, 0
min_y, max_y = R-1, 0

# sink 지도를 탐색하여 땅('X')이 존재하는 최소/최대 x, y 좌표를 찾음
for y in range(R):
    for x in range(C):
        if 'X' in sink[y][x]:
            min_x = min(x, min_x)
            max_x = max(x, max_x)
            min_y = min(y, min_y)
            max_y = max(y, max_y)

# 계산된 범위 내에서 50년 후의 지도 출력
for y in range(min_y, max_y + 1):
    print("".join(sink[y][min_x:max_x+1]))
