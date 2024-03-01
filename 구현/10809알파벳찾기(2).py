# s=input()

# alpa=[]

# for i in range(97,123):
#     alpa.append(i)

# for i in range(len(alpa)):
#     if chr(alpa[i]) in s:
#         alpa[i] = s.index(chr(alpa[i]))
#     else:
#         alpa[i] = '-1'

# for i in range(len(alpa)):
#     print(alpa[i], end=' ')

s=input()

alpa=[]

for i in range(97,123):
    alpa.append(i)

for i in range(len(alpa)):
    if chr(alpa[i]) in s:
        print(s.index(chr(alpa[i])),end=' ')
    else:
        print('-1',end=' ')

# for i in range(len(alpa)):
#     print(s.find(chr(alpa[i])), end=' ')