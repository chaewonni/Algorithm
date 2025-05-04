import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
questions = list(list(map(int, input().split())) for _ in range(n))

candidates = list(permutations('123456789', 3))

def calculate_score(target, guess):
    strike, ball = 0, 0
    for i in range(3):
        if target[i] == guess[i]:
            strike += 1
        if guess[i] in target:
            ball += 1
    return strike, ball


cnt = 0
for candidate in candidates:
    candidate = ''.join(candidate)
    is_valid = True
    for question, s, b in questions:
        strike, ball = calculate_score(candidate, str(question))

        if strike != s or ball != b:
            is_valid = False
    if is_valid:
        cnt += 1

print(cnt)