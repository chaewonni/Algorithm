def sol(start, end, level):
    if start == end:
        ans[level].append(tree[start])  # 현재 요소를 해당 레벨의 정답 리스트에 추가
        return

    center = (start + end) // 2  # 중앙 인덱스를 계산
    ans[level].append(tree[center])  # 중앙 요소를 해당 레벨의 정답 리스트에 추가
    
    # 왼쪽 하위 트리의 재귀적 호출
    if start <= center - 1:
        sol(start, center - 1, level + 1)
    
    # 오른쪽 하위 트리의 재귀적 호출
    if center + 1 <= end:
        sol(center + 1, end, level + 1)

# 레벨 입력 받기
Level = int(input())

# 트리 요소들을 입력받아 정수 리스트로 변환
tree = list(map(int, input().split()))

l = len(tree)  # 트리 리스트의 길이
ans = [[] for _ in range(Level)]  # 각 레벨에 대한 빈 리스트로 초기화된 정답 리스트

# 루트에서 재귀적 해결 시작
sol(0, l - 1, 0)

# 레벨별 요소 출력
for a in ans:
    print(*a)
