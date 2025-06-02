import sys
import heapq
input = sys.stdin.readline

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dijkstra(r, c, rupee, distance, seq):
    que = []
    heapq.heappush(que, (rupee[r][c], (r,c)))
    distance[r][c] = rupee[r][c]

    while que:
        dist, coordinate = heapq.heappop(que)

        r = coordinate[0]
        c = coordinate[1]

        if r == len(rupee)-1 and c == len(rupee)-1:
            print(f'Problem {seq}: {distance[r][c]}')
            break

        if distance[r][c] < dist:
            continue

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < len(rupee) and 0 <= nc < len(rupee):
                cost = dist + rupee[nr][nc] 
                if cost < distance[nr][nc]:
                    distance[nr][nc] = cost
                    heapq.heappush(que, (cost, (nr, nc)))

seq = 0

while True:
    N = int(input())
    if N == 0:
        sys.exit()

    seq += 1

    rupee = [list(map(int, input().split())) for _ in range(N)]

    distance = [[float('inf') for _ in range(len(rupee))] for _ in range(len(rupee))]

    dijkstra(0, 0, rupee, distance, seq)