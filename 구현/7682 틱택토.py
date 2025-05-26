import sys
input = sys.stdin.readline

def check_win(player, lst):
    for i in range(3):
        if lst[i][0] == lst[i][1] == lst[i][2] == player:
            return True
        if lst[0][i] == lst[1][i] == lst[2][i] == player:
            return True
    if lst[0][0] == lst[1][1] == lst[2][2] == player:
        return True
    if lst[0][2] == lst[1][1] == lst[2][0] == player:
        return True
    return False

while True:
    munja = input().strip()

    if munja == 'end':
        break
    
    lst = [[] for _ in range(3)]
    for i in range(3): # 0 / 1 / 2
        for j in range(3): # 0 1 2 / 3 4 5 / 6 7 8
            lst[i].append(munja[3 * i + j])

    o = 0
    x = 0

    result = False

    for i in range(3):
        for j in range(3):
            if lst[i][j] == 'O':
                o += 1
            elif lst[i][j] == 'X':
                x += 1
    
    x_win = check_win('X', lst)
    o_win = check_win('O', lst)

    if x == o + 1 and x_win and not o_win: # X승
        result = True
    elif x == o and o_win and not x_win: # O승
        result = True
    elif not o_win and not x_win and x + o == 9 and x == o + 1: #
        result = True

    print('valid' if result else 'invalid')