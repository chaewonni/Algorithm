def solve():
    N = int(input())
    length = 4 * N -3
    map = [[' '] * length for _ in range(length)]

    def recur(n, x, y):
        length = 4 * n - 3
        if length == 1:
            map[x][y] = "*"
            return 
        for i in range(length):
            map[x][y + i] = "*"
            map[length-1+x][y + i] = "*"
            map[y+i][x] = "*"
            map[y+i][length-1+x] = "*"
        x = x+2
        y = y+2
        return recur(n-1, x, y)


    recur(N, 0, 0)
    for i in range(length):
        print(''.join(map[i]))

solve()