data='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
#이게 겁나게 중요했던 문제
#.index잘써보기

N,B=input().split(" ")
B=int(B)
n_list=[]

n_list=list(N)

#for char in s:
#    n_list.append(char) 필요없었다....

result=0

for i in range(len(N)):
    num=data.index(n_list[len(N)-1-i])*B**i
    result+=num

print(result)
