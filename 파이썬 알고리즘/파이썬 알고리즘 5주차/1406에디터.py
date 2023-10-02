# from collections import deque

# d = deque()

# s = input()
# N = len(s)
# L = N
# for i in range(N):
#     d.append(s[i])

# print(d)
# M= int(input())

# for i in range(M):
#     com = input()
#     c_list = list(com.split())
#     if c_list[0] == "L":
#         if L == 0:
#             continue
#         else:
#             L -= 1
#     elif c_list[0] == "D":
#         if L == N:
#             continue
#         else:
#             L += 1
#     elif c_list[0] == "B":
#         if L == 0:
#             continue
#         else:
#             d.pop


from collections import deque
import sys

d1 = deque()
d2 = deque()

input = sys.stdin.readline

s = input().rstrip() ##rstrip 매우 중요

for i in s:
    d1.append(i)

M = int(input())

for i in range(M):
    com = input()
    c_list = list(com.split())
    if c_list[0] == "L":
        if len(d1) == 0:
            continue
        else:
            d2.appendleft(d1.pop())
    elif c_list[0] == "D":
        if len(d2) == 0:
            continue
        else:
            d1.append(d2.popleft())
    elif c_list[0] == "B":
        if len(d1) == 0:
            continue
        else:
            d1.pop()
    elif c_list[0] == "P":
        d1.append(c_list[1])

output = ''.join(map(str, d1+d2)) ## 이 부분도 넘넘 중요
print(output)
sys.stdout.flush()