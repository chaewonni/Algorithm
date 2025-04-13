import sys
import copy
input = sys.stdin.readline

# N: 미로 크기 (N x N), M: 참가자 수, K: 제한 시간
N, M, K = map(int, input().split())

# miro: 미로 상태를 저장하는 2차원 리스트
# 0: 빈 칸 (이동 가능), 1~9: 벽 (내구도 있음), -1: 출구
miro = [list(map(int, input().split())) for _ in range(N)]

# people: 참가자들의 초기 위치 리스트 (입력은 1-based 좌표)
people = [list(map(int, input().split())) for _ in range(M)]

# 출구 위치 (입력은 1-based 좌표)
exit = [list(map(int, input().split()))]

# 좌표를 0-based로 변환 (내부 계산을 쉽게 하기 위함)
for i in range(len(people)):
    people[i][0] -= 1
    people[i][1] -= 1
exit[0][0] -= 1
exit[0][1] -= 1

# 상, 하, 좌, 우를 나타내는 방향 벡터 (우선순위: 상 → 하 → 좌 → 우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 참가자들의 총 이동 거리 누적 변수
total_distance = 0

# ▶ 모든 참가자들이 한 턴에 한 칸씩 이동하는 함수
def move():
    global people, total_distance
    new_people = []  # 이동 결과를 저장할 새 리스트

    for r, c in people:
        if [r, c] == exit[0]:
            continue  # 이미 출구에 도달한 참가자는 무시

        moved = False  # 이동했는지 여부를 나타내는 플래그

        # 4방향 탐색 (상, 하, 좌, 우 순서)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 이동하려는 좌표가 미로 범위 내에 있고,
            # 벽이 아니며, 출구가 아닌 빈 칸일 경우만 이동 고려
            if 0 <= nr < N and 0 <= nc < N:
                if miro[nr][nc] == 0 and [nr, nc] != exit[0]:
                    now_dist = abs(exit[0][0] - r) + abs(exit[0][1] - c)      # 현재 위치에서 출구까지 거리
                    next_dist = abs(exit[0][0] - nr) + abs(exit[0][1] - nc)  # 이동 후 위치에서 출구까지 거리

                    # 이동 후 출구와 더 가까워지면 이동
                    if next_dist < now_dist:
                        new_people.append([nr, nc])  # 이동
                        total_distance += 1          # 이동 거리 누적
                        moved = True
                        break  # 첫 이동 가능한 방향으로만 이동 (우선순위)

        if not moved:
            new_people.append([r, c])  # 이동할 수 없다면 제자리

    # 출구에 도달한 참가자는 제외하고 people 리스트 갱신
    people = [p for p in new_people if p != exit[0]]

# ▶ 출구와 참가자를 포함하는 가장 작은 정사각형을 회전시키는 함수
def rotate():
    global miro, people, exit

    min_len = 999  # 최소 정사각형 길이 (1x1~N*N)
    start_r = start_c = -1  # 정사각형의 좌상단 좌표

    # 모든 가능한 정사각형 크기를 시도 (작은 정사각형부터 큰 정사각형까지)
    for size in range(1, N + 1):
        for r in range(N - size + 1):  # 정사각형의 좌상단 r 좌표
            for c in range(N - size + 1):  # 정사각형의 좌상단 c 좌표
                contains_exit = False
                contains_people = False

                # 해당 정사각형 안에 출구와 참가자가 있는지 확인
                for i in range(r, r + size):
                    for j in range(c, c + size):
                        if [i, j] == exit[0]:
                            contains_exit = True
                        if [i, j] in people:
                            contains_people = True

                # 조건을 만족하는 정사각형 중 최소 크기, 우선순위 기준으로 선택
                if contains_exit and contains_people:
                    if size < min_len:
                        min_len = size
                        start_r, start_c = r, c
                    elif size == min_len:
                        if r < start_r or (r == start_r and c < start_c):
                            start_r, start_c = r, c
        if min_len != 999:
            break  # 가장 작은 정사각형을 찾았으면 더 이상 탐색 X

    # 선택된 정사각형 영역을 sub에 복사
    sub = [[0] * min_len for _ in range(min_len)]
    for i in range(min_len):
        for j in range(min_len):
            sub[i][j] = miro[start_r + i][start_c + j]

    # 시계 방향으로 90도 회전
    new_sub = list(zip(*sub[::-1]))

    # 벽이면 내구도 1 감소 (최소 0까지)
    for i in range(min_len):
        for j in range(min_len):
            if 1 <= new_sub[i][j] <= 9:
                new_sub[i][j] -= 1

    # 회전된 결과를 다시 miro에 적용
    for i in range(min_len):
        for j in range(min_len):
            miro[start_r + i][start_c + j] = new_sub[i][j]

    # 참가자 위치도 회전된 좌표로 갱신
    new_people = []
    for r, c in people:
        # 해당 정사각형 내부에 있는 참가자만 회전
        if start_r <= r < start_r + min_len and start_c <= c < start_c + min_len:
            nr = r - start_r
            nc = c - start_c
            new_r = start_r + nc
            new_c = start_c + (min_len - 1 - nr)
            new_people.append([new_r, new_c])
        else:
            new_people.append([r, c])  # 바깥 참가자는 그대로
    people = new_people

    # 출구 좌표도 회전
    r, c = exit[0]
    if start_r <= r < start_r + min_len and start_c <= c < start_c + min_len:
        nr = r - start_r
        nc = c - start_c
        new_r = start_r + nc
        new_c = start_c + (min_len - 1 - nr)
        exit[0] = [new_r, new_c]

# ▶ 시뮬레이션 루프 (최대 K초 동안 반복)
for _ in range(K):
    if len(people) == 0:
        break  # 모든 참가자가 탈출했으면 종료

    move()  # 참가자 이동

    if len(people) == 0:
        break  # 이동 후 모두 탈출했으면 종료

    rotate()  # 미로 회전

# ▶ 결과 출력
# 1. 참가자들의 총 이동 거리
# 2. 최종 출구 좌표 (출력은 다시 1-based로 변환)
print(total_distance)
print(exit[0][0] + 1, exit[0][1] + 1)
