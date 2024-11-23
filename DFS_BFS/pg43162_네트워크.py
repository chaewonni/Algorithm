def solution(n, computers):
    answer = 0
    cnt = 0
    
    visited = [False] * (n+1)
    
    def dfs(computers, node, visited):
        print(n)
        visited[node] = True
        for i in range(1, n+1):
            print(i, computers[n-1][i-1], visited[i])
            if i != node and computers[node-1][i-1] == 1 and not visited[i]:
                dfs(computers, i, visited)
    
    for i in range(1,n+1):
        print(visited[i])
        if not visited[i]:
            cnt += 1
            dfs(computers, i, visited)
            
    return cnt