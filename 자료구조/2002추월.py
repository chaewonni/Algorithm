N = int(input())

car_in = {}
car_out = {}

for i in range(N):
    car_in[input()] = i

for j in range(N):
    car_out[input()] = j

cnt = 0
car_list = list(car_out)
for i in range(N):
    for j in range(i+1, N):
        # print(car_in[car_list[i]], car_in[car_list[j]])
        if car_in[car_list[i]] > car_in[car_list[j]]:
            cnt += 1
            break

print(cnt)