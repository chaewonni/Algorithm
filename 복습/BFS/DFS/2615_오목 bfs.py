import sys
from collections import deque
input = sys.stdin.readline

omok = [list(map(int, input().split())) for _ in range(19)]

# 아래, 오른쪽 아래 대각선, 오른쪽, 오른쪽 위 대각선
dx = [1, 1, 0, -1]
dy = [0 ,1, 1, 1]

def bfs(x,y,color,k):
    queue = deque([[x,y,1]])

    while queue:
        x,y,depth = queue.popleft()
        if depth == 5:
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < 19 and 0 <= ny < 19 and omok[nx][ny] == color:
                return 0
            return depth
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < 19 and 0 <= ny < 19 and omok[nx][ny] == color:
            queue.append([nx,ny,depth+1])
    return 0


for i in range(19):
    for j in range(19):
        if omok[i][j] != 0:
            for k in range(4):
                if bfs(i,j,omok[i][j],k) == 5:
                    nx, ny = i - dx[k], j - dy[k]
                    if 0 <= nx < 19 and 0 <= ny < 19 and omok[nx][ny] == omok[i][j]:
                        continue

                    print(omok[i][j])
                    print(i+1,j+1)
                    sys.exit(0)
print(0)