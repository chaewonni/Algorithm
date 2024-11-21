import sys
input = sys.stdin.readline

N, M = map(int, input().split())

chess = [list(input().rstrip()) for _ in range(N)]
lst = []

for i in range(N-7):
    for j in range(M-7):
        w_index = 0 # 'W'로 시작할 경우 바뀐 체스 판의 갯수
        b_index = 0
        for ii in range(i, i+8):
            for jj in range(j, j+8):
                if (ii+jj) % 2 == 0:
                    if chess[ii][jj] != 'W':
                        w_index += 1
                    if chess[ii][jj] != 'B':
                        b_index += 1
                else:
                    if chess[ii][jj] != 'W':
                        b_index += 1
                    if chess[ii][jj] != 'B':
                        w_index += 1
        lst.append(min(b_index, w_index))

print(min(lst))