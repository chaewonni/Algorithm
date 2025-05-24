# bfs가 아니고 그리디네..

import sys
input = sys.stdin.readline

N = int(input())
original = list(input().strip())
want = list(input().strip())

def toggle(lst, idx):
    for i in [idx - 1, idx, idx +1]:
        if 0 <= i < len(lst):
            if lst[i] == '0':
                lst[i] = '1'
            else:
                lst[i] = '0'

def count_switches(original, want, press_first):
    original_copy = original[:]
    cnt = 0
    if press_first:
        toggle(original_copy, 0)
        cnt += 1

    for i in range(1, len(original_copy)):
        if original_copy[i-1] != want[i-1]:
            toggle(original_copy, i)
            cnt += 1

    if original_copy == want:
        return cnt
    else:
        return float('inf')

press = count_switches(original, want, True)
not_press = count_switches(original, want, False)

result = min(press, not_press)
print(result if result != float('inf') else -1)