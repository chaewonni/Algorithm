import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * (N+1)

result = []
team1 = []

people = [i for i in range(N)]

def dfs(idx, total):
    
    if N//2 == total:
        # 팀 능력치 구하는 로직?
        team2 = list(set(people) - set(team1))
        
        team1_sum = 0
        team2_sum = 0
        
        for i in team1:
            for j in team1:
                if i != j :
                    team1_sum = team1_sum + S[i][j]
                
        for i in team2:
            for j in team2:
                if i != j:
                    team2_sum = team2_sum + S[i][j]
                
        result.append(abs(team1_sum-team2_sum))
        return
    
    for num in range(idx, N):
        if not visited[num]:
            visited[num] = True
            team1.append(num)
            dfs(num, total + 1)
            visited[num] = False
            team1.pop()
    
dfs(0, 0)
print(min(result))