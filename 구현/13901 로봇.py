import sys
input = sys.stdin.readline

R, C = map(int, input().split())
maps = [list('*' * C) for _ in range(R)]
k = int(input())

for _ in range(k):
    br, bc = map(int, input().split())
    maps[br][bc] = 'x'

sr, sc = map(int, input().split())
direction = list(map(int, input().split()))

# 위, 아래, 왼, 오
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

current_dir = 0

def decide_direction(sr, sc, current_dir):
    if direction[current_dir] == 1:
        return sr + dr[0], sc + dc[0]
    elif direction[current_dir] == 2:
        return sr + dr[1], sc + dc[1]
    elif direction[current_dir] == 3:
        return sr + dr[2], sc + dc[2]
    else:
        return sr + dr[3], sc + dc[3]
    
cnt = 0
maps[sr][sc] = cnt
no = 0
while True:
    if no == 4:
        print(sr, sc)
        sys.exit()
    
    nr, nc = decide_direction(sr, sc, current_dir)
    
    if 0 <= nr < R and 0 <= nc < C: 
        if maps[nr][nc] == '*':
            cnt += 1
            maps[nr][nc] = cnt
            sr, sc = nr, nc
            no = 0
        else:
            current_dir = (current_dir + 1) % 4
            no += 1
    else:
        current_dir = (current_dir + 1) % 4
        no += 1    