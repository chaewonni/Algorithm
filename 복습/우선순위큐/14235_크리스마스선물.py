import sys
import heapq
input = sys.stdin.readline

present = []
n = int(input())

for _ in range(n):
    a = input().strip()
    if a == '0':
        if not present:
            print("-1")
        else:
            print(-heapq.heappop(present))
    else:
        plus = list(map(int, a.split()))
        for i in range(1,plus[0]+1):
            heapq.heappush(present, -plus[i])