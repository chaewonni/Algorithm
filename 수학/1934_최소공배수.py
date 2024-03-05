T = int(input())   # 유클리드 호제법

for i in range(T):  
    a, b = map(int,input().split())
    # 유클리드 호제법을 사용하기 위한 초기값 설정
    x, y = a, b
    # y가 0이 아닐 때까지 반복
    while y != 0:
        # x 값을 임시 변수에 저장
        temp = x
        # y 값을 x에 할당
        x = y
        # x를 y로 나눈 나머지를 y에 할당
        y = temp % y
    # 최대공약수(x)를 이용해 최소공배수를 계산하고 출력
    # 최소공배수는 a와 b의 곱을 최대공약수로 나눈 값
    print(a * b // x)
