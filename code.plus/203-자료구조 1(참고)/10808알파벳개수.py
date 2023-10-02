n=input()
alphabet_list = []
zero_list = []

for i in range(97,123):
    alphabet_list.append(i)
    zero_list.append(0)

for i in range(len(n)):
    if(ord(n[i]) in alphabet_list):
        zero_list[ord(n[i]) - 97] += 1

for i in range(len(zero_list)):
    print(zero_list[i])


#ord는 abc~를 97,98,99로 바꿔주는 함수
