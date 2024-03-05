# 두 개의 정수 M과 N을 입력받음
M, N = map(int, input().split(' '))

# N+1까지의 수에 대해 소수 여부를 저장할 배열 생성, 초기값은 모두 True
n = N + 1
array = [True] * n
# 1은 소수가 아니므로 False로 설정
array[1] = False

# 에라토스테네스의 체 알고리즘 구현
# 2부터 n의 제곱근까지 모든 수에 대해
for i in range(2, int(n ** 0.5) + 1):
    # i가 소수인 경우
    if array[i] == True:
        # i의 배수들을 False로 설정하여 소수가 아님을 표시
        for j in range(i*2, n, i):
            array[j] = False

# M부터 N까지의 모든 수에 대해
for i in range(M, N + 1):
    # 소수인 경우 출력
    if array[i] == True:
        print(i)
