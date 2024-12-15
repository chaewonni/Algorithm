def solve():
    n = int(input())

    if (n % 5) % 2 != 0: # 홀수이면
        num = n // 5 -1
        if num < 0:
            return -1
        n = n - 5*num
        num += n // 2
        return num
    else:
        num = n // 5
        n = n - 5 * num
        num += n // 2
        return num
    
print(solve())