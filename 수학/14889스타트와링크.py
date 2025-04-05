import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

people = [i for i in range(N)]
result = []

# 조합은 튜플 형태로 나오는건지?
for team1 in combinations(people, N//2):
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
    
print(min(result))