import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())

# 양분의 양
A = list(list(map(int, input().split())) for _ in range(N))
# 나무 정보 (x, y, 나이)
info = list(list(map(int, input().split())) for _ in range(M))
info.sort()

trees = [[deque() for _ in range(N)] for _ in range(N)]

for x, y, age in info:
    trees[x-1][y-1].append(age)

# 위, 아래, 왼, 오, 위왼 대각선, 위오 대각선, 아래왼 대각선, 아래오 대각선
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

# 땅 (기본 양분 5로 차있는 땅)
land = list(list(5 for _ in range(N)) for _ in range(N))

for _ in range(K):
    # 봄
    dead = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not trees[i][j]:
                continue
            
            survived = deque()
            for age in trees[i][j]:
                if land[i][j] >= age:
                    land[i][j] -= age
                    # 큐를 순회하면서 요소를 삭제하는 것은 위험하므로 새로운 survived에 저장
                    survived.append(age + 1)
                else:
                    dead[i][j].append(age)
            trees[i][j] = survived
    
    # 여름 (봄에 죽은 나무가 양분으로 변함)
    for i in range(N):
        for j in range(N):
            if not dead[i][j]:
                continue
            
            land[i][j] += sum(age // 2 for age in dead[i][j])
    
    # 가을
    for i in range(N):
        for j in range(N):
            if not trees[i][j]:
                continue
            
            for age in trees[i][j]:
                if age % 5 == 0:
                    for k in range(8):
                        nr = dr[k] + i
                        nc = dc[k] + j
                    
                        if 0 <= nr < N and 0 <= nc < N:
                            trees[nr][nc].appendleft(1)
                        
    # 겨울
    for i in range(N):
        for j in range(N):
            land[i][j] += A[i][j]
            
# K년 후 살아있는 나무의 개수
cnt = 0
for i in range(N):
    for j in range(N):
        if trees[i][j]:
            cnt += len(trees[i][j])
            
print(cnt)  
          
# 이 문제는 deque를 써서 따로 trees 배열을 저장하는 걸 생각했어야 하는 문제.
# 봄에 survived 배열과 dead 배열도 따로 만들었어야 하는거를 생각했어야함.
# 순회 하면서 그 배열을 삭제하는 것은 위험하기 때문에 따로 deque를 만들어야함.