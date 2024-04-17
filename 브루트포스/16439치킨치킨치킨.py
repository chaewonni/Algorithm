import sys
from itertools import combinations

# 입력 받기
n, m = map(int, sys.stdin.readline().strip().split())
preferences = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

# 최대 선호도 합
max_preference_sum = 0

# 모든 조합의 아이템 트리플렛 탐색
for combo in combinations(range(m), 3):
    current_sum = 0
    # 각 학생에 대해 최대 선호도를 계산
    for prefs in preferences:
        # 현재 조합에서 최대 선호도 합을 구함
        current_sum += max(prefs[combo[0]], prefs[combo[1]], prefs[combo[2]])
    # 최대 선호도 합 업데이트
    max_preference_sum = max(max_preference_sum, current_sum)

# 최대 선호도 출력
print(max_preference_sum)