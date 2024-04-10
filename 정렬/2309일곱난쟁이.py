height = []
real = []

for _ in range(9):
    height.append(int(input()))

total_height = sum(height)

found = False
for i in range(8):
    if found:
        break
    for j in range(i+1, 9):

        if total_height - height[i] - height[j] == 100:
            # 높은 인덱스 부터 삭제
            height.remove(height[j])
            height.remove(height[i])
            found = True
            break

height.sort()

for i in height:
    print(i)


# import itertools

# array = [int(input()) for _ in range(9)]

# for i in itertools.combinations(array, 7):  
#     if sum(i) == 100:  
#         for j in sorted(i):  
#             print(j)
#         break 