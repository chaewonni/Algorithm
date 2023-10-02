# from collections import deque

# d = deque()
# n=int(input())

# for i in range(n):
#     s=input()
#     s_list=s.split(" ")
#     if s_list[0] == 'push_back':
#         d.append(s_list[1]) #덱의 뒤에 추가
#     elif s_list[0] == 'push_front':
#         d.appendleft(s_list[1]) #덱의 앞에 추가
#     elif s_list[0] == 'pop_front':
#         if len(d) == 0:
#             print("-1")
#         else:
#             print(d.popleft())
#     elif s_list[0] == 'pop_back':
#         if len(d) == 0:
#             print("-1")
#         else:
#             print(d.pop())
#     elif s_list[0] == 'size':
#         print(len(d))
#     elif s_list[0] == 'empty':
#         if len(d) == 0:
#             print("1")
#         else:
#             print("0")
#     elif s_list[0] == 'front':
#         if len(d) == 0:
#             print("-1")
#         else:
#             print(d[0])
#     elif s_list[0] == 'back':
#         if len(d) == 0:
#             print("-1")
#         else:
#             print(d[-1])

#코드가 시간초과 되는 이유는 'input()'함수를 사용하여 입력을 받을 때
#매번 호출할 때마다 입력 대기 상태에 있어서 생기는 문제

#이런 상황에서는 입력을 미리 받아두고 처리하는 방식을 사용하여 
#시간을 줄일 수 있음

from collections import deque
import sys

d = deque()
n=int(sys.stdin.readline().strip())

for i in range(n):
    s= sys.stdin.readline().strip()
    s_list=s.split(" ")
    if s_list[0] == 'push_back':
        d.append(s_list[1]) #덱의 뒤에 추가
    elif s_list[0] == 'push_front':
        d.appendleft(s_list[1]) #덱의 앞에 추가
    elif s_list[0] == 'pop_front':
        if len(d) == 0:
            print("-1")
        else:
            print(d.popleft())
    elif s_list[0] == 'pop_back':
        if len(d) == 0:
            print("-1")
        else:
            print(d.pop())
    elif s_list[0] == 'size':
        print(len(d))
    elif s_list[0] == 'empty':
        if len(d) == 0:
            print("1")
        else:
            print("0")
    elif s_list[0] == 'front':
        if len(d) == 0:
            print("-1")
        else:
            print(d[0])
    elif s_list[0] == 'back':
        if len(d) == 0:
            print("-1")
        else:
            print(d[-1])
