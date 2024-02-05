N = int(input())

dp = [0]*N

num_list = list(map(int, input().split()))

dp = [x for x in num_list]

for i in range(1,N):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i], dp[j]+num_list[i])

print(max(dp))