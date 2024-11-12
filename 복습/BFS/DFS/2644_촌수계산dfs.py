import sys
input = sys.stdin.readline

n = int(input())
A, B = map(int, input().split())
m = int(input())

g = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a,b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

def dfs(g, n, visited, depth):
    if n == B:
        return depth
    visited[n] = True
    for num in g[n]:
        if not visited[num]:
            result = dfs(g, num, visited, depth+1)
            if result != -1: # 값이 없으면 다른 인접 노드들도 탐색을 해야 하는데 얘가 없으면 그냥 반환해버림
                return result
    return -1

result = dfs(g, A, visited, 0)
print(result)