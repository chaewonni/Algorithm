# import sys

# s = sys.stdin.readline

# num1, num2 = map(int, s().split())

# a = max(num1, num2)
# b = min(num1, num2)

# n_list=[]
# for i in range(1, b+1):
#     if b % i == 0:
#         n_list.append(i)

# for i in range(len(n_list)):
#     if a % n_list[i] == 0:
#         cd = n_list[i]

# cs = num1*num2//cd
# print(cd)
# print(cs)

import sys
import math

s = sys.stdin.readline

num1, num2 = map(int, s().split())

print(math.gcd(num1, num2))
print(math.lcm(num1, num2))




