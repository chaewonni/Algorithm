import sys

N = int(sys.stdin.readline())

# candy = [for _ in range(N) [for _ in range(N)]]

candy = []
maxCandy = 0

for i in range(N):
    candy.append(list(sys.stdin.readline().strip()))

def row():
    global maxCandy
    for i in range(N):
        count = 1
        for j in range(N-1):
            if candy[i][j] == candy[i][j+1]:
                count += 1
                maxCandy=max(maxCandy, count)
            else:
                count = 1

def column():
    global maxCandy
    for j in range(N):
        count = 1
        for i in range(N-1):
            if candy[i][j] == candy[i+1][j]:
                count += 1
                maxCandy=max(maxCandy,count)
            else:
                count = 1

for i in range(N):
    for j in range(N-1):
        if candy[i][j] != candy[i][j+1]:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            row()
            column()
            candy[i][j+1], candy[i][j] = candy[i][j], candy[i][j+1]
        if candy[j][i] != candy[j+1][i]:
            candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]
            row()
            column()
            candy[j+1][i], candy[j][i] = candy[j][i], candy[j+1][i]

print(maxCandy)

