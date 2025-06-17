import sys
import copy
input = sys.stdin.readline

N, M, R = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

layers = min(N, M) // 2

for layer in range(layers):
    elements = []
    top, left = layer, layer
    bottom, right = N-layer-1, M-layer-1

    # 위쪽 가로
    for c in range(left, right + 1):
        elements.append(A[top][c])
    
    # 오른쪽 세로
    for r in range(top + 1, bottom):
        elements.append(A[r][right])

    # 아래쪽 가로
    for c in range(right, left - 1, -1):
        elements.append(A[bottom][c])

    # 왼쪽 세로
    for r in range(bottom - 1, top, -1):
        elements.append(A[r][left])

    rot = R % len(elements)
    rotated = elements[rot:] + elements[:rot]


    for c in range(left, right + 1):
        A[top][c] = rotated.pop(0)
    for r in range(top + 1, bottom):
        A[r][right] = rotated.pop(0)
    for c in range(right, left - 1, -1):
        A[bottom][c] = rotated.pop(0)
    for r in range(bottom -1, top, -1):
        A[r][left] = rotated.pop(0)

for row in A:
    print(*row)