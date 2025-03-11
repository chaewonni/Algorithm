import sys
input = sys.stdin.readline

C, R = map(int, input().split())
K = int(input())

concert = [[0] * R for _ in range(C)]

# y가 커짐, x가 커짐, y가 작아짐, x가 작아짐
dx = [0, 1, 0, -1] 
dy = [1, 0, -1, 0]

x, y = 1, 1

direction = 0

for i in range(1, R*C+1):
    concert[x-1][y-1] = i
    
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 1 <= nx <= C and 1 <= ny <= R and concert[nx-1][ny-1] == 0:
        x, y = nx, ny
    else:
        direction = (direction + 1) % 4
        x, y = x + dx[direction], y + dy[direction]
    
    
for i in range(C):
    for j in range(R):
        if concert[i][j] == K:
            print(i+1, j+1)
            sys.exit()
            
print(0)

import sys
input = sys.stdin.readline

C, R = map(int, input().split())
K = int(input())

concert = [[0] * R for _ in range(C)]

# y가 커짐, x가 커짐, y가 작아짐, x가 작아짐
dx = [0, 1, 0, -1] 
dy = [1, 0, -1, 0]

x, y = 1, 1  
direction = 0

for i in range(1, R * C + 1):
    concert[x-1][y-1] = i  

    if i == K:  
        print(x, y)  
        sys.exit(0)

    nx, ny = x + dx[direction], y + dy[direction]

    if not (1 <= nx <= C and 1 <= ny <= R and concert[nx-1][ny-1] == 0):
        direction = (direction + 1) % 4
        nx, ny = x + dx[direction], y + dy[direction]

    x, y = nx, ny  
    
print(0)
