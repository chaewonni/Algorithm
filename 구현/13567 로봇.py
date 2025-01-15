import sys
input = sys.stdin.readline

M, n = map(int, input().split())

robot = []
for _ in range(n):
    command, num = input().split()
    robot.append((command, int(num)))

# 초기화
x, y = 0, 0
idx = 0
directions = ['east', 'north', 'west', 'south']

def check_boundary(new_x, new_y):
    if not (0 <= new_x < M and 0 <= new_y < M):
        print(-1)
        sys.exit(0)

for command, num in robot:
    if command == 'MOVE':
        if directions[idx] == 'east':
            check_boundary(x + num, y) 
            x += num
        elif directions[idx] == 'north':
            check_boundary(x, y + num)  
            y += num
        elif directions[idx] == 'west':
            check_boundary(x - num, y) 
            x -= num
        elif directions[idx] == 'south':
            check_boundary(x, y - num)
            y -= num
    elif command == 'TURN':
        if num == 0:
            idx = (idx + 1) % 4  # 좌회전
        elif num == 1:
            idx = (idx - 1 + 4) % 4  # 우회전
        else:
            print(-1)
            sys.exit(0)
    else:
        print(-1)
        sys.exit(0)

print(x, y)
