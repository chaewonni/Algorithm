import sys
import heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, time = map(int, input().split())
    graph[start].append((time, end))

def dijkstra(num):
    distance = [(10e9) for _ in range(N+1)]
    queue = []
    heapq.heappush(queue, (0, num))

    while queue:
        cost, n = heapq.heappop(queue)

        if distance[n] < cost:
            continue
        
        for g in graph[n]:
            dist = g[0]

            new_cost = cost + dist
            if distance[g[1]] > new_cost:
                distance[g[1]] = new_cost
                heapq.heappush(queue, (new_cost, g[1]))

    return distance

result = [(10e9) for _ in range(N+1)]
result[0] = 0
for i in range(1, N+1):
    if i == X:
        result[i] = 0
        continue

    distance = dijkstra(i)
    result[i] = distance[X]

    distance = dijkstra(X)
    result[i] += distance[i]

print(max(result))