import sys
input = sys.stdin.readline

N, A, B = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort(reverse=True)
arr2.sort(reverse=True)
ans, idx1, idx2 = 0, 0, 0

# 홀수일 경우
if N % 2 == 1:
    ans += arr1[0]
    arr1.pop(0)
    
for _ in range(N // 2):
    case1, case2 = 0, 0
    if len(arr1) >= 2:
        case1 = arr1[0] + arr1[1]
    if len(arr2) >= 1:
        case2 = arr2[0]
        
    if case1 > case2:
        ans += case1
        arr1.pop(0)
        arr1.pop(0)
    else:
        ans += case2
        arr2.pop(0)

print(ans)