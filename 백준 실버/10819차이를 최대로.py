# def solve():
#     N = int(input())
#     nums = list(map(int, input().split()))
#     answer = []

#     visited = [False] * N

#     def dfs(result):
#         if len(result) == N:
#             cnt = 0
#             for i in range(1,N): # 1 2 3 4 5
#                 cnt += abs(result[i-1] - result[i])
#             answer.append(cnt)
#             return
        
#         for i in range(N):
#             if not visited[i]:
#                 visited[i] = True
#                 result.append(nums[i])
#                 dfs(result)
#                 result.pop()
#                 visited[i] = False

#     dfs([])
#     print(max(answer))

# solve()


def solve():
    N = int(input())
    nums = list(map(int, input().split()))
    answer = []

    def dfs(nums, n, visited):
        visited[n] = True
        if len(result) == N:
            cnt = 0
            for i in range(1,N): # 1 2 3 4 5
                cnt += abs(result[i-1]- result[i])
                answer.append(cnt)
            return
        for i in range(len(nums)):
            if not visited[i]:
                result.append(nums[i])
                dfs(nums, i, visited)
                result.pop()
                visited[i] = False

    for i in range(N):
        result = []
        visited = [False] * (N)
        result.append(nums[i])
        dfs(nums, i, visited)

    print(max(answer))

solve()