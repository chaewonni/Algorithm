import sys
input = sys.stdin.readline

N, K, P, X = map(int, input().split())

SEGMENT = [
    0b1111110,  # 0
    0b0110000,  # 1
    0b1101101,  # 2
    0b1111001,  # 3
    0b0110011,  # 4
    0b1011011,  # 5
    0b1011111,  # 6
    0b1110000,  # 7
    0b1111111,  # 8
    0b1111011   # 9
]

# 9 1 2 5
# 1~9층까지 이용 가능, 디스플레이에 1자리 수 보임, 최대 2개 반전 가능, 실제로 5층

lst = []

answer = 0

for x in str(X).zfill(K):
    lst.append(SEGMENT[int(x)])

# 48 2 5 35
for i in range(1, N+1): # 1 ~ 48
    total = 0

    if i == X:
        continue
    
    target = str(i).zfill(K) # 바꾸려는 층

    for idx in range(K):
        a = lst[idx] # 현재 층 X의 LED 상태
        b = SEGMENT[int(target[idx])] # 바꾸려는 층 i의 LED 상태

        total += bin(a^b).count('1')

    if 1 <= total <= P:
        answer += 1

print(answer)