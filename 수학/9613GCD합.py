import sys
import math
input = sys.stdin.readline

t = int(input())

for i in range(t):
    sum = 0
    s = input()
    s_list = list(map(int, s.split()))
    for i in range(1, len(s_list)-1):
        for j in range(i+1, len(s_list)):
            gcd = math.gcd(s_list[i], s_list[j])
            sum += gcd
    print(sum)