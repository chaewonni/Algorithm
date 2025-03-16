def solve():
    K = int(input())
    stack = []

    for _ in range(K):
        num = int(input())
        if num == 0 and stack:
            stack.pop()
        else:
            stack.append(num)

    return sum(stack)

print(solve())