def solve():
    N, M = map(int, input().split())

    result = []

    def dfs():
        if len(result) == M:
            print(' '.join(map(str, result)))
            return
        for num in range(1, N+1):
            result.append(num)
            dfs()
            result.pop()
    dfs()
solve()