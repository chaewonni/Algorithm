N=int(input())

P=[]
P=input().split(" ")
P=list(map(int,P)) #P = list(map(int, input().split()))
r=[0]*(N+1)

for i in range(1,N+1): #만약 i가 4라면
    price=10000
    for j in range(1,i+1): #카드 4장을 갖기 위해 지불해야 하는 금액의 최댓값 구하는 반복
        price = min(price, P[j-1]+r[i-j]) #max(0원,카드 1장+ 3장 살때 max price)
        r[i]=price                      #max(max price, 카드 2장 + 카드 2장 살 때 max price)
                                        #max(max price, 카드 3장 + 카드 1장 살 때 max price)
print(r[N])                             #max(max price, 카드 4장)