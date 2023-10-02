T=int(input())

hap=[0]*11

for i in range(T):
    n=int(input())

    for i in range(n+1):
        if i==1:
            hap[1]=1
        elif i==2:
            hap[2]=2
        elif i==3:
            hap[3]=4
        else:
            hap[i]=hap[i-1]+hap[i-2]+hap[i-3]

    print(hap[n])

# 1은 1개, 2는 2개, 3은 4개, 4는 7개, 5는 13개
# n>3부터 hap[n]=hap[n-1]+hap[n-2]+hap[n-3]