import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]

dx = [-1, 0, 1, 1]
dy = [1, 1, 1, 0]

for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            color = board[i][j]
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                cnt = 1

                while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
                    cnt += 1

                    if cnt == 5:
                        if 0 <= i - dx[k] < 19 and 0 <= j - dy[k] < 19 and board[i - dx[k]][j - dy[k]] == color:
                            break
                        if 0 <= nx + dx[k] < 19 and 0 <= ny + dy[k] < 19 and board[nx + dx[k]][ny + dy[k]] == color:
                            break

                        print(color)
                        print(i+1, j+1)
                        sys.exit(0)

                    nx = nx + dx[k]
                    ny = ny + dy[k]

print(0)