def solution(m, n, puddles): # x:n, y:m
    answer = 0
    dp = [[0] * m for _ in range(n)]
    # print(dp)
        
        
    for i in range(n):
        for j in range(m):
            if [j+1, i+1] in puddles:
                dp[i][j] = 0
            else:  
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007

    answer = dp[n-1][m-1]
    return answer