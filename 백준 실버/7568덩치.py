def solve():
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    result = []

    for x, y in lst:
        cnt = 0
        for i in range(N):
            if x < lst[i][0] and y < lst[i][1]:
                cnt += 1
        result.append(cnt+1)

    print(' '.join(map(str, result)))
solve()