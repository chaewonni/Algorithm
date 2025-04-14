import sys
input = sys.stdin.readline

N = int(input())

length = list(map(int, input().split()))
grow = list(map(int, input().split()))

# zip = 여러 개의 리스트를 튜플 형태로 묶어줌
trees = sorted(zip(grow, length))

cnt = 0
sum = 0
for key, value in trees:
    sum += key * cnt + value
    cnt += 1
    
print(sum)                        