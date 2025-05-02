import sys
import bisect
input = sys.stdin.readline

N, M = map(int, input().split())

dot = sorted(map(int, input().split()))

for _ in range(M):
    a, b = map(int, input().split())
    print(bisect.bisect_right(dot, b) - bisect.bisect_left(dot, a))