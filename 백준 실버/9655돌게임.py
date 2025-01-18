def solve():
    N = int(input())

    if N % 2 == 0:
        winner = 'CY'
    else:
        winner = 'SK'

    return winner
print(solve())