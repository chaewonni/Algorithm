from collections import deque

def solve():
    N, M = map(int, input().split())
    miro = [list(map(int,input())) for _ in range(N)]

    dx = [0, 0, -1, 1] #왼, 오, 위, 아래
    dy = [-1, 1, 0, 0]

    def bfs(x,y):
        queue = deque([(x,y)])

        while queue:
            x,y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
            
                if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] == 1:
                    queue.append((nx,ny))
                    miro[nx][ny] = miro[x][y] + 1
            
        return miro[N-1][M-1]

    print(bfs(0,0))
solve()