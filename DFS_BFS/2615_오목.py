import sys
input = sys.stdin.readline

g = [list(map(int, input().split())) for _ in range(19)]

directions = [(0,1), (1,0), (1,1), (-1,1)]

def isValid(nx, ny):
    return 0 <= nx < 19 and 0 <= ny < 19

def dfs(x,y,color,direction,count):
    nx = x + direction[0]
    ny = y + direction[1]

    if isValid(nx, ny) and g[nx][ny] == color:
        return dfs(nx,ny,color,direction,count+1)
    return count

for i in range(19):
    for j in range(19):
        if g[i][j] == 1 or g[i][j] == 2:
            for direction in directions:
                if dfs(i,j,g[i][j],direction,1) == 5:
                    px, py = i - direction[0], j - direction[1]
                    if isValid(px, py) and g[px][py] == g[i][j]:
                        continue
                    print(g[i][j])
                    print(i + 1, j + 1)  
                    sys.exit(0)  

print(0)