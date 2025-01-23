import sys
input = sys.stdin.readline

A, K = map(int, input().split())
cnt = 0

while K > A:
    if K % 2 == 0:
        if K // 2 < A:
            K = K - 1   
        else :
            K = K // 2 
    else:
        K = K -1
    cnt += 1
    
print(cnt)