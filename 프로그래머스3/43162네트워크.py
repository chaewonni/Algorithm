def solution(n, computers):
    answer = 0
    visited = [False] * (n+1)
    
    g = [[] * len(computers) for _ in range(len(computers))]
    
    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if i != j and computers[i][j] == 1:
                g[i].append(j)
    
    def dfs(i):
        nonlocal answer
        visited[i] = True
        for j in g[i]:
            if not visited[j]:
                print(j)
                dfs(j)
        
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer