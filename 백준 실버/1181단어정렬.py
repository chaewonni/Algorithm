def solve():
    N = int(input())
    lst = set()

    for i in range(N):
        lst.add(input().strip())

    sorted_lst = sorted(lst, key=lambda x: (len(x),x))

    for sl in sorted_lst:
        print(sl)

solve()