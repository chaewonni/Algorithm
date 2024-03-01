lst = []

for i in range(5):
    row = [' '] * 15
    lst.append(row)

for i in range(5):
    s=input()
    for j in range(len(s)):
        lst[i][j] = s[j]

result = ""

for i in range(15):        
    for j in range(5):
        if lst[j][i] != ' ':
            result += lst[j][i]
        else:
            continue

print(result)