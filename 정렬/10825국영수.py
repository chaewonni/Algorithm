N = int(input())
score = []
for _ in range(N):
    score.append(input().split())

# 이 튜플의 순서대로 정렬 기준이 적용
score.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(N):
    print(score[i][0])