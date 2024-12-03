# import sys
# input = sys.stdin.readline

# # DOG
# # GOD GOOD DOLL

# N = int(input())

# # DGO
# # D:1 G:1 O:1

# # DGO DGOO DLLO  + DG DA DAO DOOO
# # D:1 G:1 O:1
# # D:1 G:1 O:2
# # D:1 L:2 O:1

# # dict의 key가 같거나
# # 
# result = 0
# lst = []
# for _ in range(N):
#     lst.append(sorted(input().strip()))

# for i in range(1,N):
#     cnt = 0
#     if len(lst[0]) > len(lst[i]): #DOG 랑 DA, DOG랑 DG
#         for s in lst[0]:  # 첫번째꺼
#             if s not in lst[i]: 
#                 cnt += 1
#     else: #DOG 랑 GOD, #DOG랑 GOOD #DOG 랑 DOLL
#         for s in lst[i]:
#             if s not in lst[0]:
#                 cnt += 1

#     if cnt > 1:
#         result += 1


# print(N-1-result)

import heapq
import sys
input = sys.stdin.readline

# 한 단어에서 한 문자 더하거나, 빼거나,
# 하나의 문자를 다른 문자로 바꾸어  

n = int(input())
cnt = 0

word = list(input().strip())

for i in range(n-1):
    s_cnt = 0
    compare = list(input().strip())

    for c in word[:]:
        if c in compare:
            compare.remove(c)
        else:
            s_cnt += 1 # 이게 관건이었음

    if len(compare) < 2 and s_cnt < 2:
        cnt += 1

print(cnt)