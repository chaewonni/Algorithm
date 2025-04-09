import sys
import copy
input = sys.stdin.readline

# 각 칸의 색깔 1이상 10 이하의 숫자로 표현 

# 위 아래 왼 오
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

n = int(input())
nums = list(list(map(int, input().split())) for _ in range(n))
nums_copy = copy.deepcopy(nums)

# 초기 예술 점수는 모든 그룹 쌍의 조화로움의 합
# 초기 예술 점수 구한 뒤에는 그림에 대한 회전
# 십자 모양의 경우 통째로 반시계 방향 (얘는 통째로 반시계 방향 회전하고, 그 십자 모양에 해당하는 애들만 저장하는식)
# 나머지는 개별적으로 시계 방향으로 90도 (for 해서 십자 전까지...? 더 좋은 방법 생각해보기)

# 초기 예술 점수 + 1회전 이후 예술 점수 + 2회전 이후 예술 점수 + 3회전 이후 예술 점수
total_score = 0

# 행, 열, 칸에 있는 숫자
def dfs(r, c, num, visited, groups):

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n:
            if nums[nr][nc] == num and not visited[nr][nc]: # 같은 그룹
                visited[nr][nc] = True
                groups.append((nr, nc))
                dfs(nr, nc, num, visited, groups)

# 그룹 구하기
# groups: 같은 수인 애들 묶음, total_groups: 전체 애들 묶음
def group():
    visited = [[False] * n for _ in range(n)]
    total_groups = []

    for r in range(n):
        for c in range(n):
            # dfs 함수 호출
            if not visited[r][c]:
                groups = [(r, c)]
                visited[r][c] = True
                dfs(r, c, nums[r][c], visited, groups)
                total_groups.append((nums[r][c], groups))

    return total_groups


# 예술 점수 구하기 (그림판)
# 초기 예술 점수는 모든 그룹 쌍의 조화로움의 합
# return score 할 수 있음 좋겠다
# 각 조합 예술 점수 합산
def sum_score(nums):
    score = 0

    # 그룹 구하기 함수 호출
    total_groups = group()
    # print(total_groups)

    combinations = []
    for i in range(len(total_groups)-1):
        for j in range(i+1, len(total_groups)):
            combinations.append((i,j))

    # print(combinations)
    
    for a, b in combinations: # [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
        len_a = len(total_groups[a][1])
        len_b = len(total_groups[b][1])
        num_a = total_groups[a][0]
        num_b = total_groups[b][0]

        # a랑 b의 맞닿아 있는 변의 수
        cnt = 0
        for a1, a2 in total_groups[a][1]:
            for b1, b2 in total_groups[b][1]:
                if (a1 == b1 and abs(a2 - b2) == 1) or (a2 == b2 and abs(a1 - b1) == 1):
                    cnt += 1
        score += (len_a + len_b) * num_a * num_b * cnt
    return score

# 회전
# 십자 모양의 경우 통째로 반시계 방향 (얘는 통째로 반시계 방향 회전하고, 그 십자 모양에 해당하는 애들만 저장하는식)
# 나머지는 개별적으로 시계 방향으로 90도 (for 해서 십자 전까지...? 더 좋은 방법 생각해보기)
def rotate():
    global nums_copy

    # 십자 모양 회전
    center = len(nums_copy) // 2

    sub = list(row[::-1] for row in nums_copy)
    nums_copy = list(zip(*sub))

    for r in range(n):
        for c in range(n):
            if r == center or c == center: # 십자 모양일 때만
                nums[r][c] = nums_copy[r][c]

    # 십자 제외 회전: 시계 방향 90도
    # 왼쪽 위 회전
    sub = [[0] * center for _ in range(center)]
    for r in range(0, center):
        for c in range(0, center):
            sub[r][c] = nums[r][c]

    new_sub = [list(row) for row in zip(*sub[::-1])]

    for r in range(0, center):
        for c in range(0, center):
            nums[r][c] = new_sub[r][c]

    # 왼쪽 밑 회전
    sub = [[0] * center for _ in range(center)]
    for r in range(0, center):
        for c in range(0, center):
            sub[r][c] = nums[r + center + 1][c]

    new_sub = [list(row) for row in zip(*sub[::-1])]

    for r in range(0, center):
        for c in range(0, center):
            nums[r + center + 1][c] = new_sub[r][c]

    # 오른쪽 위 회전
    sub = [[0] * center for _ in range(center)]
    for r in range(0, center):
        for c in range(0, center):
            sub[r][c] = nums[r][c + center + 1]

    new_sub = [list(row) for row in zip(*sub[::-1])]

    for r in range(0, center):
        for c in range(0, center):
            nums[r][c + center + 1] = new_sub[r][c]

    # 오른쪽 아래 회전
    sub = [[0] * center for _ in range(center)]
    for r in range(0, center):
        for c in range(0, center):
            sub[r][c] = nums[r + center + 1][c + center + 1]

    new_sub = [list(row) for row in zip(*sub[::-1])]

    for r in range(0, center):
        for c in range(0, center):
            nums[r + center + 1][c + center + 1] = new_sub[r][c]

total_score = sum_score(nums)
#1회전
rotate()
total_score += sum_score(nums)
#2회전
rotate()
total_score += sum_score(nums)
#3회전
rotate()
total_score += sum_score(nums)

print(total_score)