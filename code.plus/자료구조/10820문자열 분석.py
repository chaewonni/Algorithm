n=int(input())


for i in range(n):
    super = 0
    slower = 0
    integer = 0
    space = 0
    s = input()
    for i in s:
        if i.isupper():
            super += 1
        elif i.islower():
            slower += 1
        elif i == ' ':
            space += 1
        else:
            integer += 1


    print(slower, super, integer, space)


# while True:
#     try:
#         super, slower, integer, space = 0, 0, 0, 0
#         s = input()
#         for i in s:
#             if i.isupper():
#                 super += 1
#             elif i.islower():
#                 slower += 1
#             elif i == ' ':
#                 space += 1
#             else:
#                 integer += 1
#         print(slower, super, integer, space)
#     except EOFError:
#         break
        