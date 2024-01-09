n=int(input())

sik=input()
list=[]
stack=[]

for i in range(n):
    list.append(int(input()))

for i in sik:
    if 'A' <= i <= 'Z': #연산자 만나면
        stack.append(list[ord(i)-ord('A')])
    else: #피연산자 만나면
        a=stack.pop()
        b=stack.pop()
        if i == '+':
            stack.append(b+a)
        elif i == '-':
            stack.append(b-a)
        elif i == '*':
            stack.append(b*a)
        elif i == '/':
            stack.append(b/a)

print('%.2f' %stack[0])

