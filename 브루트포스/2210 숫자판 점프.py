import sys
input = sys.stdin.readline

math_arr = [list(map(int, input().split())) for _ in range(5)]

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

result = set()

def dfs(x, y, num):
    if len(num) == 6:
        result.add(num)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
            
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, num + str(math_arr[nx][ny]))

for i in range(5):
    for j in range(5):    
        dfs(i, j, str(math_arr[i][j]))
        
print(len(result))