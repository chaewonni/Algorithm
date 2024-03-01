n=input()
list=[]
for i in range(1, len(n)+1): #range함수는 끝 인덱스를 포함하지 않는 범위 반환
    list.append(n[-i:])
print(*sorted(list), sep='\n') 
#*은 unpacking연산자. 반환된 리스트의 모든 요소를
#개별적인 인자로 unpacking하겠다
#정렬된 리스트의 요소들을 개별적인 인자로 출력하며, 
# 이때 요소들 사이에는 개행문자('\n')가 들어간다는 의미

n=input()
list=[]
for i in range(1, len(n)+1): #range함수는 끝 인덱스를 포함하지 않는 범위 반환
    list.append(n[-i:])
list=sorted(list)

for i in range(len(list)):
    print(list[i])