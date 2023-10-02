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


for i in range(len(list)):
    if list[0] == 0:
        list.remove(0)


if len(list) == 0:
    print(0)
else:
    print(''.join(map(str, list)))

#bin() : 10진수를 2진수로 바꿔주고, 접두어 '0b'가 붙는다.

#oct(): 10진수를 8진수로 바꿔주고, 접두어 '0o'가 붙는다.

#hex(): 10진수를 16진수로 바꿔주고, 접두어 '0x' 가 붙는다.

#print(bin(int(input(),8))[2:])