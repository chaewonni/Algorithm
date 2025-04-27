import sys
import math
input = sys.stdin.readline

N = int(input())
A = map(int, input().split())
B, C = map(int, input().split())

cnt = 0

for a in A:
    a -= B
    cnt += 1
    
    if a > 0:    
        cnt += math.ceil(a / C)        
print(cnt)