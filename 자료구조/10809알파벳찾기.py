# n=input()

# #아스키 코드로 알파벳 리스트 만들기
# data = list(range(97,123))

# for i in data:
#     print(n.find(chr(i)))


# n=input()

# data='abcdefghijklmnopqrstuvwxyz'
# data=list(data)

# for i in data:
#     print(n.find(i))


n=input()

data_list= []

for i in range(97,123):
    data_list.append(i)

for i in data_list:
    print(n.find(chr(i)))

