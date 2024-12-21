def solve():
    N, M = map(int, input().split())
    nums = [i for i in range(1, N+1)]

    visited = [False] * (N+1)
    result = []

    def dfs():
        if len(result) == M:
            print(' '.join(map(str, result)))
        for num in nums:
            if not visited[num]:
                visited[num] = True
                result.append(num)
                dfs()
                result.pop()
                visited[num] = False

    dfs()
solve()
