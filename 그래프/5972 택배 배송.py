import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B,C))
    graph[B].append((A,C))

distance = [INF] * (N+1)

# 다익스트라
def dijkstra(start):
    distance[start] = 0
    
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, node = heapq.heappop(queue)

        if distance[node] < dist:
            continue

        for next_node, cost in graph[node]:
            new_cost = dist + cost

            if distance[next_node] > new_cost:
                distance[next_node] = new_cost 
                heapq.heappush(queue, (new_cost, next_node))

dijkstra(1)
print(distance[N])