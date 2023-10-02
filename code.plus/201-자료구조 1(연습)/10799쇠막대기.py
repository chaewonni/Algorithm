# n=input()

# stack=[]
# num = 0

# n_list=list(n) #이거 넘넘 중요하다 제발

# for i in range(len(n_list)):
#     if n_list[i]=="(":
#         stack.append(n_list[i])
#     elif n_list[i]==")":
#         if len(stack)!=0:
#             stack.pop()
#             if n_list[i-1] == "(":
#                 for i in range(len(stack)):
#                     num += 1
#             else:
#                 num += 1
# print(num)

n=input()

stack=[]
num = 0

for i in range(len(n)):
    if n[i]=="(":
        stack.append(n[i])
    elif n[i]==")":
        if len(stack)!=0:
            stack.pop()
            if n[i-1] == "(": # 이 부분만 알았어도...!
                num += len(stack)
            else:
                num += 1
print(num)