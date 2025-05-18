from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = deque(map(int, input().split()))

# 로봇이 올라가는 윗줄만 관리
robots = deque([False] * N)
step = 0

while True:
    step += 1

    # 1. 벨트와 로봇 함께 회전
    A.rotate(1)
    robots.rotate(1)
    robots[-1] = False # 내리는 위치에 도달한 로봇 제거

    # 2. 로봇 이동
    for i in range(N-2, -1, -1):
        if robots[i] and not robots[i+1] and A[i+1] > 0:
            robots[i+1] = True
            robots[i] = False
            A[i+1] -= 1
    robots[-1] = False

    # 3. 로봇 올리기
    if A[0] > 0:
        robots[0] = True
        A[0] -= 1

    # 4. 내구도 0인 칸의 개수 K개 이상이면 과정 종료
    if A.count(0) >= K:
        print(step)
        break