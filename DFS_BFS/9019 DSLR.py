import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    def bfs(num):
        visited = [False] * 10000
        queue = deque([(num, [])])
        visited[num] = True

        while queue:
            num, path = queue.popleft()

            if num == B:
                return path

            # D
            new_num = num * 2 % 10000
            if not visited[new_num]:
                queue.append((new_num, path + ['D']))
                visited[new_num] = True

            # S
            if num == 0:
                new_num = 9999
            else:
                new_num = num - 1
            if not visited[new_num]:
                queue.append((new_num, path + ['S']))
                visited[new_num] = True

            # L
            new_num = (num % 1000) * 10 + num // 1000
            if not visited[new_num]:
                queue.append((new_num, path + ['L']))
                visited[new_num] = True

            # R
            new_num = (num % 10) * 1000 + (num // 10) 
            if not visited[new_num]:
                queue.append((new_num, path + ['R']))
                visited[new_num] = True
        
    result = bfs(A)
    for r in result:
        print(r, end='')
    print()