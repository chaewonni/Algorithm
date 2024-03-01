# s=input()

# list=[]

# for i in range(len(s)):
#     list.append(ord(s[i])+13)

# for i in range(len(list)):
#     print(chr(list[i]))

s=input()

list=[]

for i in range(len(s)):
    x = ord(s[i])
    if (65 <= x and x <= 77) or (97 <= x and x <= 109): #A~M 은 N~Z, a~m 은 n~z
        list.append(chr(x+13))
    elif (78<= x and x <=90) or (110 <= x and x <= 122): #N~Z 는 A~M, n~z 는 a~m
        list.append(chr(x-13))
    else: # 공백
        list.append(chr(x)) 

print(''.join(list))


# s=list(input())

# for i in range(len(s)):
#     x = ord(s[i])
#     if (65 <= x and x <= 77) or (97 <= x and x <= 109):
#         s[i] = chr(x+13)
#     elif (78<= x and x <=90) or (110 <= x and x <= 122):
#         s[i] = chr(x-13)

# print(''.join(s))
