import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    lst = []
    n = int(input())
    for i in range(n):
        lst.append(input().strip())

    lst.sort()
    is_prefix = False

    for i in range(len(lst)-1):
        if lst[i+1].startswith(lst[i]):
            print("NO")
            is_prefix = True
            break
    if not is_prefix:
        print("YES")