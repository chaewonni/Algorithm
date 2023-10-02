s=input()

num_list = [int(digit) for digit in s]
list=[]

for i in range(len(num_list)):
    num=num_list[i]//4
    list.append(num)
    num2=(num_list[i]-num*4)//2
    list.append(num2)
    num3=(num_list[i]-num*4-num2*2)//1
    list.append(num3)

if(''.join(map(str,list[0:3])) != '000'):
    for i in range(len(list)):
        if(list[0]==0):
            list.remove(0)
            #del list[0]

if len(list) == 0:
    print(0)
else:
    print(''.join(map(str, list)))


