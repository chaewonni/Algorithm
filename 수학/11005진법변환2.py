data='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N,B=input().split(" ")
N=int(N)
B=int(B)
n_list=[]

while(N > 0):
    num=N%B
    N=N//B
    if(num>=10):
        n_list.append(data[num])
    else:
        n_list.append(str(num))
    
n_list=list(reversed(n_list))
print(''.join(n_list))