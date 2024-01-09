N = int(input())

arr = []
max = 0
min = 10

swap = 0

for i in range(10):
    num = int(input())
    arr.append(num)

# arr = sorted(arr)

cnt = 0

for i in range(10):
    for j in range(9):
        if arr[j] > arr[j+1]:
            swap = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = swap
        cnt= cnt+1

for i in range(10):
    print(arr[i])

# for i in range(10):
#     print(arr[i])

