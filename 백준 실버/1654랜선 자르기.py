def solve():
    K, N = map(int, input().split())
    k_lst = []
    for _ in range(K):
        k_lst.append(int(input()))

    start = max(k_lst) // N
    end = sum(k_lst) // N

    answer = 0

    while start <= end:

        mid = (start + end) // 2
        if mid == 0:
            mid += 1
            
        cnt = 0
        for k in k_lst:
            cnt += k // mid
            
        if cnt >= N:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    
    print(answer)
solve()