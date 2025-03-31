import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y, cost = map(int, input().split())
    graph[x].append((y,cost))
    
A, B = map(int, input().split())

# 다익스트라
distance = [int(1e9) for _ in range(N+1)]

def dijkstra(num):
    que = []
    heapq.heappush(que, (0, num))
    distance[num] = 0
    
    while que:
        # dist: 현재 정점까지의 거리
        # now: 현재 탐색할 정점
        dist, now = heapq.heappop(que)
        
        if distance[now] < dist:
            continue
        
        for node in graph[now]:
            weight = node[1]
            next_node = node[0]
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(que, (cost, next_node))
    
dijkstra(A)
print(distance[B])