# 주어진 문자의 키보드 좌표 반환
def get_coordinate(char, keyboard):
    for i, row in enumerate(keyboard):
        if char in row:
            return (i, row.index(char))

# 키보드 레이아웃 정의
keyboard = [
    ['z', 'x', 'c', 'v', 'b', 'n', 'm'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
]

left_initial, right_initial = input().split()
input_string = input()

# 초기 손가락 위치 설정
left_pos = get_coordinate(left_initial, keyboard)
right_pos = get_coordinate(right_initial, keyboard)

total_time = 0  # 입력에 소요된 총 시간

# 입력 문자열 처리
for char in input_string:
    char_pos = get_coordinate(char, keyboard)
    
    # 오른손으로 입력하는 경우 판단
    if (char_pos[0] == 0 and char_pos[1] >= 4) or char_pos[1] >= 5:
        total_time += abs(right_pos[0] - char_pos[0]) + abs(right_pos[1] - char_pos[1]) + 1
        right_pos = char_pos
    else:  # 왼손으로 입력하는 경우
        total_time += abs(left_pos[0] - char_pos[0]) + abs(left_pos[1] - char_pos[1]) + 1
        left_pos = char_pos

print(total_time)
