import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = sorted(set(list(map(int, input().split()))))

result = []

def dfs(start):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(start, len(K)):
        result.append(K[i])
        dfs(i)
        result.pop()

dfs(0)