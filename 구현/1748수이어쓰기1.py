# import sys

# N = int(sys.stdin.readline())

# num = 1

# for i in range(2,N+1):
#    num = str(num) + str(i)

# print(len(num))



# 1~9 -> 1*9*10^0 = 9자리
# 10~99 -> 2*9*10^1 = 180자리
# 100~999 -> 3*9*10^2 = 2700자리 .......

# n * 9 * 10**(n-1)


import sys

num = int(sys.stdin.readline())

n = len(str(num))  # num의 길이 구하기 

length = 0

for i in range(1,n):
    length += i * 9 * 10**(i-1)   
    #만약 num이 3자리라면 2자리까지는 일단 다 더하기
    #만약 124라면 2자리까지 (1~99)는 다 더하고,

length = length + (num - 10**(n-1) + 1) * n   

    #124-100+1=25 남은 (100~124) 25개는 3자리수이므로 25*3

print(length)
