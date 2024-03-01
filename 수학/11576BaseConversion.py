A,B=input().split(" ")
A=int(A)
B=int(B)
m=int(input())

a_list=list(input().split(" ")) #A진법 입력받음
a_list=list(map(int, a_list))   #map함수 이용해서 list숫자들 int로 바꿔줌
a_list=list(reversed(a_list))   #reversed해줌

t_num=0

#A진법에서 10진법으로 바꿈
for i in range(m):
    num=a_list[i]*(A**i)
    t_num+=num

#10진법에서 B진법으로 바꿈
b_list=[]

while(t_num>0):
    remainder=t_num%B
    t_num=t_num//B
    b_list.append(remainder)

b_list=list(map(str, b_list))
b_list=list(reversed(b_list))
print(" ".join(b_list))

