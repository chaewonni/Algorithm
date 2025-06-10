import sys
input = sys.stdin.readline

N, M, L, K = map(int, input().split())
star = [list(map(int, input().split())) for _ in range(K)]

max_cnt = 0

# K = 1인 경우 고려 못함
for i in range(len(star)):
    for j in range(len(star)):
        cnt = 0
        x = star[i][0]
        y = star[j][1]

        for sx, sy in star:
            if x <= sx <= x + L and y <= sy <= y + L:
                cnt += 1

        max_cnt = max(max_cnt, cnt)

print(K - max_cnt)