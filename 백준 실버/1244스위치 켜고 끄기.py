def solve():
    N = int(input())
    switch = list(map(int, input().split()))

    student = int(input())

    for _ in range(student):
        sex, num = map(int, input().split())

        if sex == 1:
            for i in range(N, 0, -1):
                if i % num == 0:
                    if switch[i-1] == 0:
                        switch[i-1] = 1
                    else:
                        switch[i-1] = 0
        else:
            if switch[num-1] == 0:
                switch[num-1] = 1
            else:
                switch[num-1] = 0
            for i in range(1, N//2+1):
                if num-i-1>=0 and num+i-1<=N-1:
                    if switch[num-i-1] == switch[num+i-1]:
                        if switch[num-i-1] == 1:
                             switch[num-i-1], switch[num+i-1] = 0,0
                        else:
                            switch[num-i-1], switch[num+i-1] = 1,1
                    else:
                        break

    cnt = 0
    for i in range(len(switch)):
        print(switch[i], end=' ')
        cnt += 1
        if cnt == 20:
            print()
            cnt = 0
solve()

