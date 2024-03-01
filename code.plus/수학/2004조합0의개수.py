# n, m = map(int, input().split())

# nf=1 
# mf=1

# for i in reversed(range(1,n+1)):
#     nf = nf * i

# for i in reversed(range(1,m+1)):
#     mf = mf * i

# cha = n-m
# chaf = 1

# for i in reversed(range(1,cha+1)):
#     chaf = chaf * i

# num = nf/mf*chaf

# print(num)

# num = str(num)
# print(num)

n, m = map(int, input().split())

def two(num):
    two_cnt = 0
    n=1
    i=2
    while n != 0:
        n = num // i
        two_cnt += n
        i = i * 2
    return two_cnt

def five(num):
    five_cnt = 0
    n=1
    i=5
    while n != 0:
        n = num // i
        five_cnt += n
        i = i * 5
    return five_cnt

a = two(n) - two(m) - two(n-m)
b = five(n) - five(m) - five(n-m)

print(min(a,b))
