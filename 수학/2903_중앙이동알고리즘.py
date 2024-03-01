N = int(input())

data = list(range(16))
data[0] = 2
data[1] = 3

for i in range(2,16):
    data[i] = data[i-1] * 2 - 1


print(data[N]*data[N])