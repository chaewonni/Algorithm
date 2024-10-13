import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num_list = []
visited = [False] * (N+1)

def dfs():
    if len(num_list) == M:
        print(' '.join(map(str, num_list)))
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = True
        num_list.append(i)
        dfs()
        visited[i]=False
        num_list.pop()

dfs()