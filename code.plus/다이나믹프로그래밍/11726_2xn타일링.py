n=int(input())

sum=[0]*1001

for i in range(1,n+1):
    if i==1:
        sum[1]=1
    elif i==2:
        sum[2]=2
    else:
        sum[i]=sum[i-1]+sum[i-2]

print(sum[n]%10007)