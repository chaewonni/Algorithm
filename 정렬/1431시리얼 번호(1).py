import sys

N = int(sys.stdin.readline())

serial = []

# 주어진 문자열 s에서 숫자들의 합을 계산하는 함수
def sum_of_digits(s):
    total = 0
    for char in s:
        if char.isdigit():
            total += int(char)
    return total

for i in range(N):
    serial.append(sys.stdin.readline().strip())

# serial 리스트의 요소를 정렬 기준에 따라 정렬
# 1. 요소(시리얼 번호)의 길이가 짧은 것부터
# 2. 요소 내 숫자들의 합이 작은 것부터
# 3. 사전순
serial.sort(key = lambda x:(len(x), sum_of_digits(x), x))

for i in serial:
    print(i)