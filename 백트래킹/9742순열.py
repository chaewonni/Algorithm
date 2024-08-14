import sys

input = sys.stdin.readline

def dfs(string, i):
    global cnt
    if i == len(A):
        cnt += 1
        if cnt == B:
            return string
        
    else:
        for k in A:
            if k not in string:
                res = dfs(string + k, i+1)
                if res:
                    return res
                
    return
                

while 1:
    cnt = 0
    A,B = input().rstrip().split()
    B = int(B)

    if (len(A) ** 2) < B:
        print(A, B, '=', 'No permutation')
    else:
        print(A, B, '=', dfs('', 0))