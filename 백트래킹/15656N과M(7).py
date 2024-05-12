import sys
input = sys.stdin.readline

N,M = map(int, input().split())
K = sorted(list(map(int, input().split())))

result = []

def dfs():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(len(K)):
        result.append(K[i])
        dfs()
        result.pop()

dfs()