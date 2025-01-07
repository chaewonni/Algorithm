import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
bridge = list(map(int, input().split()))
a, b = map(int, input().split())

visited = [False] * (N+1) 

def bfs(start): # start: 위치
    visited[start] = True
    queue = deque([(start, 0)]) # 현재위치, 점프 횟수
    
    while queue:
        current, jump = queue.popleft()
        
        if current == b:
            return jump
        
        num = bridge[current - 1] # 징검다리에 적힌 숫자
        
        for direction in [1, -1]:
            mul = 1
            while True:
                next_pos = current + num * mul * direction
                if next_pos < 1 or next_pos > N:  
                    break
                if not visited[next_pos]:
                    visited[next_pos] = True
                    queue.append((next_pos, jump + 1))
                mul += 1
            
    return -1


result = bfs(a)
print(result)