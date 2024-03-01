import sys

def to_decimal(string, number): #number진수 string을 10진수로 변환
    cur, res = 0,0
    for i in range(len(string)):
        if string[i].isdigit():
            cur = int(string[i])
        else:
            cur = ord(string[i]) - 97 + 10

        if cur >= number:
            return -1
        
        res += (number ** (len(string) - i - 1)) * cur

    return res


A,B = sys.stdin.readline().split()

a_temp, b_temp = [-1, -1], [-1, -1]
for i in range(2, 37):
    a_temp.append(to_decimal(A, i))
    b_temp.append(to_decimal(B, i))

res = []

for i in range(2, 37):
    for j in range(2, 37):

        if i == j:
            continue
        if a_temp[i] != -1 and a_temp[i] == b_temp[j]:
            res.append((a_temp[i], i , j))

if len(res) > 1:
    print('Multiple')
elif not res:
    print('Impossible')
else:
    print(*res[0], sep=' ') #res:언팩하여 각 요소를 개별적으로 전달