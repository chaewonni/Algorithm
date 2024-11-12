import sys
input = sys.stdin.readline

omok = []

for i in range(19):
    omok.append(list(map(int, input().split())))

# 아래, 오른쪽 아래 대각선, 오른쪽, 오른쪽 위 대각선
dx = [1, 1, 0, -1]
dy = [0 ,1, 1, 1]

def dfs(x, y, color, k, depth):
    nx = x + dx[k]
    ny = y + dy[k]
                
    if 0 <= nx < 19 and 0 <= ny < 19 and omok[nx][ny] == color:
        return dfs(nx,ny,color,k, depth+1)
    return depth


for i in range(19):
    for j in range(19):
        if omok[i][j] != 0:
            for k in range(4):
                if dfs(i, j, omok[i][j], k, 1) == 5:
                    nx, ny = i - dx[k], j - dy[k]
                    if omok[nx][ny] == omok[i][j]:
                        continue
                    
                    print(omok[i][j])
                    print(i+1, j+1)
                    sys.exit(0)

print(0)