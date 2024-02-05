n = int(input())

s_list=[]

for _ in range(n):
    s_list.append(int(input()))

dp=[[0]*3 for _ in range(n)]


for i in range(0,n):
    if i==0:
        dp[i][0] = s_list[0]
        dp[i][1] = 0
        dp[i][2] = s_list[0]
    elif i==1:
        dp[i][0] = s_list[0]
        dp[i][1] = s_list[0] + s_list[1]
        dp[i][2] = s_list[1]
    else:
        dp[i][0] = dp[i-1][1]
        dp[i][1] = dp[i-1][2] + s_list[i]
        dp[i][2] = dp[i-1][0] + s_list[i]

print(max(dp[n-1]))
        
    
