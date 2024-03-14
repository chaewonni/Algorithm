import sys
N, M = map(int, sys.stdin.readline().split())

my_string = set()

for i in range(N):
    my_string.add(sys.stdin.readline())

cnt = 0
for i in range(M):
    if sys.stdin.readline() in my_string:
        cnt += 1

print(cnt)