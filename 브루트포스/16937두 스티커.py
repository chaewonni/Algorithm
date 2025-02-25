import sys
input = sys.stdin.readline

H, W = map(int, input().split())
N = int(input())

lst = []
result = []

for _ in range(N):
    R, C = map(int, input().split())
    lst.append([R,C])
    
max_area = 0

for i in range(len(lst)-1):
    for j in range(i+1, len(lst)):
        (r1, c1) = lst[i]
        (r2, c2) = lst[j]
        
        for (nr1, nc1) in [(r1, c1), (c1, r1)]:
            for (nr2, nc2) in [(r2, c2), (c2, r2)]:
                if (nr1 + nr2 <= H) and (max(nc1, nc2) <= W):
                    max_area = max(max_area, nr1 * nc1 + nr2 * nc2)

                if (max(nr1, nr2) <= H) and (nc1 + nc2 <= W):
                    max_area = max(max_area, nr1 * nc1 + nr2 * nc2)
                    
print(max_area)