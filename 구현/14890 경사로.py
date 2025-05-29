import sys
input = sys.stdin.readline
N, L = map(int, input().split())
maps = list(list(map(int, input().split())) for _ in range(N))

# 한 줄이 통과 가능한지 확인하는 함수
def can_pass(line, L):
    # 경사로가 설치된 칸을 기록하는 배열 (겹치지 않게 하려고)
    used = [False] * len(line)
    
    # 줄의 처음부터 끝 직전까지 차례대로 비교
    for i in range(len(line) - 1):
        curr = line[i]
        next = line[i+1]
        
        # 높이가 같으면 그냥 지나갈 수 있음
        if curr == next:
            continue
        # 다음 칸이 1 더 높음 -> 오르막 경사로 설치 필요
        elif curr + 1 == next:
            # 현재 칸부터 뒤로 L칸 확인 (앞쪽에 경사로 깔 수 있는지 확인)
            for j in range(i, i - L, -1):
                # 범위를 벗어거나거나, 높이가 다르거나, 이미 경사로가 설치돼 있으면 실패
                if j < 0 or line[j] != curr or used[j]:
                    return False
                used[j] = True
        # 다음 칸이 1 더 낮음 -> 내리막 경사로 설치 필요
        elif curr - 1 == next:
            # 다음 칸부터 앞으로 L칸 확인 (뒤쪽에 경사로 깔 수 있는지 확인)
            for j in range(i + 1, i + 1 + L):
                # 범위를 벗어나거나, 높이가 다르거나, 이미 경사로가 설치돼 있으면 실패
                if j >= len(line) or line[j] != next or used[j]:
                    return False
                used[j] = True 
        # 높이 차이가 2 이상이면 경사로 설치 불가능 -> 실패
        else:
            return False
        
    # 모든 구간에서 문제 없었으면 통과 가능         
    return True          

cnt = 0

# 행 검사
for row in maps:
    if can_pass(row, L):
        cnt += 1

# 열 검사
for c in range(N):
    col = [maps[r][c] for r in range(N)]
    if can_pass(col, L):
        cnt += 1
        
print(cnt)