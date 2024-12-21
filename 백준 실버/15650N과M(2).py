def solve():
    N, M = map(int, input().split())
    nums = [i for i in range(1, N+1)]

    result = []
    visited = [False] * (N+1)

    def dfs():
        if len(result) == M:
            print(' '.join(map(str, result)))
            return
        for num in nums:
            if not visited[num]:
                if not result or result[-1] < num:
                    result.append(num)
                    visited[num] = True
                    dfs()
                    result.pop()
                    visited[num] = False

    dfs()
solve()