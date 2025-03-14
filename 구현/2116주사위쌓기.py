import sys
input = sys.stdin.readline

N = int(input())
dice = []
for _ in range(N):
    dice.append(list(map(int, input().split())))

def decide(num):
    if num == 0:
        next = 5
    elif num == 1:
        next = 3
    elif num == 2:
        next = 4
    elif num == 3:
        next = 1
    elif num == 4:
        next = 2
    elif num == 5:
        next = 0
    
    return next

def up(next):
    cnt = 0  # 같은 면의 최댓값 합
    top_value = dice[0][decide(next)]  # 첫 주사위의 윗면 값

    for i in range(N):  # 2번째 주사위부터 처리
        under = next  # 현재 밑면 인덱스
        top = decide(next)  # 현재 윗면 인덱스

        # 밑면 값 찾아서 윗면 결정
        under_value = top_value
        under = dice[i].index(under_value)
        top = decide(under)
        top_value = dice[i][top]  # 다음 주사위의 윗면 값

        # 윗면, 밑면 제외한 4개 옆면에서 최댓값 찾기
        temp_dice = dice[i][:]  
        del temp_dice[max(under, top)]
        del temp_dice[min(under, top)]
        cnt += max(temp_dice)

    return cnt

result = max(up(i) for i in range(6))
print(result)