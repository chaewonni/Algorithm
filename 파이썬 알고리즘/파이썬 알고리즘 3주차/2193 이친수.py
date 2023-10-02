N = int(input())

arr = [0]*(N+1)

arr[1] = 1 #1
if N>=2:
    arr[2] = 1 #10
if N>=3:
    arr[3] = 1 + arr[1] #101, 101

for i in range(4, N+1):
    arr[i] = arr[i-1] + arr[i-2]  

print(arr[N])

