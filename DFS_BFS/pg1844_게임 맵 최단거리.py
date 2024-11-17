from collections import deque
def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]  #위 아래 오 왼
    dy = [0, 0, 1, -1]
    
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps)) ]
    distance = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    n = len(maps)
    m = len(maps[0])
    def bfs(x,y,maps,visited):
    
        visited[x][y] = True
        distance[x][y] = 1
        queue = deque([(x,y)])
        while queue:
            a,b = queue.popleft()
            if a == n-1 and b == m-1:
                return distance[a][b]
            for i in range(4):
                nx, ny = a + dx[i], b + dy[i]
                if 0<= nx < n and 0 <= ny < m and maps[nx][ny] != 0:
                    if not visited[nx][ny]:
                        queue.append((nx,ny))
                        visited[nx][ny] = True
                        distance[nx][ny] = distance[a][b] + 1
        else:
            return -1
    answer = bfs(0,0,maps,visited)
    return answer