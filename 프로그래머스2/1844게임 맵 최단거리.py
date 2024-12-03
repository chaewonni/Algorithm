from collections import deque

def solution(maps):
    answer = 0
    
    #왼 오 위 아래
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    def bfs(x,y):
        queue = deque([(x,y)])
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                    queue.append((nx,ny))
                    maps[nx][ny] = maps[x][y] + 1
    
    bfs(0,0)
    if maps[len(maps)-1][len(maps[0])-1] == 1:
        answer = -1
    else:
        answer = maps[len(maps)-1][len(maps[0])-1]
    return answer