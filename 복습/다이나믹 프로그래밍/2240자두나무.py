import sys
input = sys.stdin.readline

T, W = map(int, input().split())

lst = []
for i in range(T):
    lst.append(int(input()))

dp = [0] * T
move = [[0] * 2 for i in range(T)]

for i in range(T):
    if i == 0:
        if lst[i] == 2:
            move[i][0] == 1
            move[i][1] == 0
            dp[0][0] = 1
            dp[0][1] = 0
        else:
            move[i][0] = 0
            move[i][1] = 0
            dp[0][0] = 1
            dp[0][1] = 1
    if i >= 1:
        if lst[i] != lst[i-1]:
            for j in range(2):
                move[i][j] = move[i-1][j] + 1
                if move[i][j] <= W:
                    dp[i][j] = dp[i-1][j] + 1 
        else:
            