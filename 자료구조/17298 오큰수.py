import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
new_lst = [-1] * len(lst)

stack = [0]

for i in range(1, len(lst)):
    num = lst[i]
    while stack and lst[stack[-1]] < lst[i]:
        new_lst[stack.pop()] = num
        
    stack.append(i) 

print(' '.join(map(str, new_lst)))