N= int(input())

dp=[]

num_list = list(map(int, input().split()))

dp.append(num_list[0])

for i in range(1,6):
    if dp[len(dp)-1] <= num_list[i]:
        dp[len(dp)-1] = num_list[i]
    else:
        dp.append(num_list[i])

print(len(dp))
