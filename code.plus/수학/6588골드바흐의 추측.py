# import sys

# while True:
#     s = sys.stdin.readline
#     for i in range(3, s):
#         for j in range(2, j):
#             if i % j == 0:
#                 continue
#             else:
#                 a = i
#                 b = s-a
#                 for i in range(2, b):
#                     if b % i == 0:
#                         break
                
#             continue


# import sys

# questionRange = 1000000
# array = [True] * (questionRange + 1)
# array[0], array[1] = False, False

# for i in range(2, int(len(array) ** 0.5) + 1):
#     for j in range(i ** 2, len(array), i):
#         array[j] = False        

# while True:
#     n = int(sys.stdin.readline())
#     if n == 0:
#         break
#     resultA, resultB = 0, questionRange+1
#     a = 0
#     b = n

#     while True:
#         if array[a] and array[b]: #만약 a,b가 모두 소수라면
#             resultA = a
#             resultB = b
#             break
#         else::
#             a += 1
#             b -= 1
#     if resultA != 0 and resultB != (questionRange + 1):
#         print(f'{n} = {resultA} + {resultB}') ## 이거 너무너무 중요
#     else:
#         print("Goldbach's conjecture is wrong.")        


import sys

n = 1000001

array = [1]*n #일단 다 소수
for i in range(3, int(n ** 0.5) + 1, 2): #2씩 증가하는 이유는 애초에 짝수들은 배수들도 다 소수가 아니니까
    if array[i]:
        for j in range(i*2, n, i):
            array[j] = 0

while 1:
    k = int(sys.stdin.readline())
    if not k: ## k가 0인 경우
        break
    for i in range(3, int(k/2) + 1, 2):
        if array[i] and array[k-i]:
            print(f'{k} = {i} + {k-i}')
            break
    else:
        print("Goldbach's conjecture is wrong.")