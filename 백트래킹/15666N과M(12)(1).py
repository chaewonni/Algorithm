import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted(set(list(map(int, input().split()))))
result = []

def dfs():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    for l in lst:
        if result:
            if result[-1] <= l:
                result.append(l)
                dfs()
                result.pop()
        else:
            result.append(l)
            dfs()
            result.pop()
        
dfs()