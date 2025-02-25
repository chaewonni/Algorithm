import sys
input = sys.stdin.readline

H, W = map(int, input().split())
N = int(input())  

lst = [list(map(int, input().split())) for _ in range(N)]  

max_area = 0  

for i in range(N - 1):
    for j in range(i + 1, N):
    
        R1, C1 = lst[i]
        R2, C2 = lst[j]

        # 1️⃣ 회전 없이 배치 가능한 경우
        if (R1 + R2 <= H and max(C1, C2) <= W) or (C1 + C2 <= W and max(R1, R2) <= H):
            max_area = max(max_area, R1 * C1 + R2 * C2)

        # 2️⃣ 두 번째 사각형을 회전한 경우
        if (R1 + C2 <= H and max(C1, R2) <= W) or (C1 + R2 <= W and max(R1, C2) <= H):
            max_area = max(max_area, R1 * C1 + R2 * C2)

        # 3️⃣ 첫 번째 사각형을 회전한 경우
        if (C1 + R2 <= H and max(R1, C2) <= W) or (R1 + C2 <= W and max(C1, R2) <= H):
            max_area = max(max_area, R1 * C1 + R2 * C2)

        # 4️⃣ 두 개 다 회전한 경우
        if (C1 + C2 <= H and max(R1, R2) <= W) or (R1 + R2 <= W and max(C1, C2) <= H):
            max_area = max(max_area, R1 * C1 + R2 * C2)

print(max_area)
