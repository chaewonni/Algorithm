import sys
import math
input = sys.stdin.readline

n = int(input())
planet = list(map(int, input().split()))

planet = list(reversed(planet))

speed = planet[0]

for i in range(n):
    if planet[i] < speed:
        speed = planet[i] * (math.ceil(speed/planet[i]))
    else:
        speed = planet[i]

print(speed)