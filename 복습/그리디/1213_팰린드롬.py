import sys
input = sys.stdin.readline

name = input().split()

dict = {}

front = ''
mid = ''

for n in name:
    dict[n] = dict.get(n,0) + 1

odd = 0

for key in sorted(dict):
    count = dict[key]
    if count % 2 == 1:
        odd += 1
        mid = key

if odd > 1:
    print("I'm sorry Hansoo")
else:
    for key in sorted(dict):
        front += key * (dict[key] // 2)
    result = front + mid + front[::-1]
    print(result)