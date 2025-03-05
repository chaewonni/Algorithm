import sys
input = sys.stdin.readline

k = int(input())
arr = list(input().split()) # > < < < > > > < <

visited = [False] * 10

result = []

def dfs(index, num, cnt):
    
    if len(num) == k+1:
        result.append(num)
        return
    
    if arr[cnt-1] == '<':
        for i in range(10):
            if not visited[i] and index < i:
                visited[i] = True
                dfs(i, num + str(i), cnt+1)
                visited[i] = False
                
    if arr[cnt-1] == '>':
        for i in range(10):
            if not visited[i] and index > i:
                visited[i] = True
                dfs(i, num + str(i), cnt+1)
                visited[i] = False
    

for i in range(10):
    visited[i] = True
    dfs(i, str(i), 1)
    visited[i] = False

print(max(result))
print(min(result))