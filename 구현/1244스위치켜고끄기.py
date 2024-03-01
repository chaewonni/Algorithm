import sys

n=int(sys.stdin.readline())

switch = list(map(int , sys.stdin.readline().split(" ")))

stu = int(sys.stdin.readline())

for i in range(stu):
    n1, n2 = map(int,sys.stdin.readline().split(" "))
    
    if n1 == 1:
        for i in range(n2, n+1, n2):
            switch[i-1] = switch[i-1]^1

    elif n1 == 2:
        cnt = 1

        while True:
            m1 = n2 - cnt
            m2 = n2 + cnt
            if m1 > 0 and m2 <= n:
                if switch[m1-1] == switch[m2-1]:
                    cnt+=1
                    continue
                else:
                    break
            else:
                break

        for i in range(m1+1, m2):
            switch[i-1] = switch[i-1]^1

cnt = 0
for i in range(len(switch)):
    print(switch[i], end=' ')
    cnt += 1
    if cnt == 20:
        print()
        cnt = 0