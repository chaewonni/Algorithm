A, B = map(int, input().split())
primes = [True] * int((B ** 0.5) + 1) 
primes_list = []

for i in range(2, int(B ** 0.5) + 1):
    if primes[i]:
        primes_list.append(i)
        for j in range(i*i, int(B ** 0.5) + 1, i):
            primes[j] = False
        

num = []
for i in primes_list:
    j = 2
    while i ** j <= B:
        if i ** j >= A:
            num.append(i ** j)  
        j += 1
            
print(len(num))