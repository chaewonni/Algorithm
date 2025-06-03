import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,cost = map(int, input().split())
    graph[a].append((b, cost))

A, B = map(int, input().split())

distance = [int(10e9) for _ in range(n+1)]
route = [[] for _ in range(n+1)]

def dijkstra(start):
    global route
    que = []
    heapq.heappush(que, (0, start, [start]))
    distance[start] = 0
    
    while que:
        dist, num, new_route = heapq.heappop(que)

        if dist > distance[num]:
            continue

        for n, cost in graph[num]:
            new_cost = dist + cost
            if distance[n] > new_cost:
                distance[n] = new_cost
                heapq.heappush(que, (new_cost, n, new_route + [n]))
                route[n] = new_route + [n]

dijkstra(A)
print(distance[B])
print(len(route[B]))
print(*route[B])