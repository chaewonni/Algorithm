import sys

T=int(sys.stdin.readline())

for i in range(T):
    n=int(sys.stdin.readline())
    s_list=[list(map(int, input().split())) for _ in range(2)]
    dp = [[0 for _ in range(n)] for _ in range(2)]

    dp[0][0] = s_list[0][0]
    dp[1][0] = s_list[1][0]

    for i in range(1,n):
        for j in range(2):
            if j == 0:
                dp[j][i] = max(dp[j][i-1], dp[j+1][i-1]+s_list[j][i])
            else:
                dp[j][i] = max(dp[j][i-1], dp[j-1][i-1]+s_list[j][i])

    print(max(dp[0][n-1], dp[1][n-1]))

print(s_list)
print(dp)
