import sys
input = sys.stdin.readline

width, height = map(int, input().split())
n = int(input())

store = []

def cal_distance(direction, distance):
    if direction == 1: # 북
        return distance
    elif direction == 2: # 남
        return width + height + (width - distance)
    elif direction == 3: # 서
        return 2 * width + height + (height - distance)
    elif direction == 4: # 동
        return width + distance

for _ in range(n):
    dir, length = map(int, input().split())
    store.append(cal_distance(dir, length))
    
d_dir, d_length = map(int, input().split())    
d_distance = cal_distance(d_dir, d_length)

total = 2 * (width + height)

total_distance = 0
for s_distance in store:
    min_distance = min(abs(d_distance - s_distance), total - abs(d_distance - s_distance))
    total_distance += min_distance

print(total_distance)