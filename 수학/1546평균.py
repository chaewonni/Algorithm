n = int(input())

s = input()
score = list(map(int,s.split(" ")))

max = 0
for i in range(len(score)):
    if max < score[i]:
        max = score[i]

for i in range(len(score)):
    score[i] = score[i]/max*100

sum = 0
for i in range(len(score)):
    sum += score[i]

print(sum/n)