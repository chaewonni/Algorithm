import sys
import heapq
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    arr[A].append((B,1))

# 다익스트라
distance = [int(1e9) for _ in range(N+1)]

result = []

def dijkstra(num):
    que = []
    heapq.heappush(que, (0, num))
    distance[num] = 0
    
    while que:
        cnt, num = heapq.heappop(que)
        
        if cnt == K:
            result.append(num)
            
        if distance[num] < cnt:
            continue
            
        for node in arr[num]:
            cost = cnt + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(que, (cost, node[0]))
            
dijkstra(X)

if result:
    result.sort()
    for i in result:
        print(i)
else:
    print(-1)