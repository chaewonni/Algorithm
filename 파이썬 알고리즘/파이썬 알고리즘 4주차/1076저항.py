arr = [['black', '0', 10**0], ['brown', '1', 10**1], ['red','2',10**2],
       ['orange','3',10**3],['yellow','4',10**4],['green','5',10**5],
       ['blue','6',10**6],['violet','7',10**7],['grey','8',10**8],['white','9',10**9]]


one = input()
two = input()
three = input()

for i in range(10):
    if arr[i][0] == one:
        first = arr[i][1]
    if arr[i][0] == two:
        second = arr[i][1]
    if arr[i][0] == three:
        third = arr[i][2]

print(int(first + second)*third)