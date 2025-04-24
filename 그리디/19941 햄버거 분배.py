import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(input().strip())

cnt = 0 
for i in range(0, N):
    if lst[i] == 'P':
        for j in range(i-K, i+K+1):
            if 0 <= j < N and lst[j] == 'H':
                lst[j] = 'X'
                cnt += 1
                break
            
print(cnt)