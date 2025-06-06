import sys
input = sys.stdin.readline

munja = input().strip()
bomb = input().strip()

stack = []

for s in munja:
    stack.append(s)

    if len(stack) >= len(bomb) and ''.join(stack[-(len(bomb)):]) == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if not stack:
    print("FRULA")
else:
    print(''.join(stack))