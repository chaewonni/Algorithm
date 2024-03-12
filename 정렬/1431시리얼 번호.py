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

for i in range(len(serial)-1):
    for j in range(i+1, len(serial)):
        # 조건 1: 두 시리얼 번호의 길이를 비교
        if len(serial[i]) > len(serial[j]):
            serial[i], serial[j] = serial[j], serial[i]

        # 조건 2: 길이가 같으면, 숫자들의 합을 비교
        elif len(serial[i]) == len(serial[j]):
            if sum_of_digits(serial[i]) > sum_of_digits(serial[j]):
                 serial[i], serial[j] = serial[j], serial[i]

             # 조건 3: 길이도 같고 숫자 합도 같으면, 사전순으로 비교
            elif sum_of_digits(serial[i]) == sum_of_digits(serial[j]):
                if serial[i] > serial[j]:
                    serial[i], serial[j] = serial[j], serial[i]                

for i in range(N):
    print(serial[i])