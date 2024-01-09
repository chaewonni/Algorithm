from collections import deque

queue = deque()

s = input()  # 사용자로부터 입력을 받습니다. 예: "11001100"
num_list = [int(digit) for digit in s] 

#s = input()
#num_list = s.split()
#num_list = list(map(int, num_list)) 뻘짓함 ㅋㅋ

if len(num_list) % 3 == 1:
    queue.append(0)
    queue.append(0)
    for i in range(len(num_list)):
        queue.append(num_list[i])

elif len(num_list) % 3 == 2:
    queue.append(0)
    for i in range(len(num_list)):
        queue.append(num_list[i])

else:
    for i in range(len(num_list)):
        queue.append(num_list[i])

e_list=[]

while len(queue) != 0:
    num1=queue.popleft()
    num2=queue.popleft()
    num3=queue.popleft()

    num=num1*4+num2*2+num3*1
    e_list.append(num)

print(''.join(map(str, e_list)))

#bin() : 10진수를 2진수로 바꿔주고, 접두어 '0b'가 붙는다.

#oct(): 10진수를 8진수로 바꿔주고, 접두어 '0o'가 붙는다.

#hex(): 10진수를 16진수로 바꿔주고, 접두어 '0x' 가 붙는다.

#print(oct(int(input(),2))[2:]) 
#입력받은 수를 10진수로 바꾸고, oct로 다시 8진수로 바꿔준다, 인덱스 2부터 출력

