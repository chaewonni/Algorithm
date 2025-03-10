import sys
input = sys.stdin.readline

N, K = map(int, input().split())

height = list(map(int, input().split()))

num = []

for i in range(N-1):
    num.append(height[i+1]-height[i])
    
num.sort()

print(sum(num[:N-K]))


# 왜 N-K인가?
# 전체 차이 개수는 N-1개
# 우리가 제거할 차이 개수는 K-1개
# 남아 있는 차이 개수는 (N-1) - (K-1) = N-K개
# 그래서 sum(num[:N-K])가 정답이 된다.