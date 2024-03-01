import sys
N, K = map(int, (input().split(" ")))

d1 = ['?']*N

num = 0

for i in range(K):
    S, alpa = input().split(" ")
    S = int(S)
    num = (num + S) % N
    if d1[num] != '?':    # 이미 알파벳이 차있는 자리에 다시 넣으려고 할 때
        if d1[num] != alpa: 
            print('!')
            break
        else:             # 그러나 넣을 자리에 있는 알파벳과 넣을 알파벳이 같다면 통과
            d1[num] = alpa
    else:
        d1[num] = alpa

if d1[num] != alpa:
    sys.exit()
else:
    for i in range(N):
        print(d1[num % N] , end='')
        if(num >= 0):
            num -= 1
        else:
            num += N-1



