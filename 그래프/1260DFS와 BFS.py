import sys
from collections import deque

input = sys.stdin.readline

def dfs(g,v,visited):
    visited[v] = True
    print(v, end=' ')
    for i in sorted(g[v]): #작은 노드부터 방문
        if not visited[i]:
            dfs(g,i,visited)

def bfs(g,v,visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(g[v]): #작은 노드부터 방문
            if not visited[i]:
                visited[i] = True
                queue.append(i)


N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

dfs(graph, V, dfs_visited)
print()
bfs(graph, V, bfs_visited)
print()

# def bfs_with_adjacency_matrix(g, start, visited):
#     queue = deque([start])
#     visited[start] = True

#     while queue:
#         current_node = queue.popleft()
#         print(current_node, end=' ')

#         # 현재 노드에서 갈 수 있는 모든 노드를 탐색
#         for neighbor in range(len(g[current_node])):
#             # 연결이 되어있고 방문하지 않은 노드라면
#             if g[current_node][neighbor] == 1 and not visited[neighbor]:
#                 visited[neighbor] = True
#                 queue.append(neighbor)