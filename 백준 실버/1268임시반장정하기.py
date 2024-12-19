def solve():
    N = int(input())
    student = [list(map(int, input().split())) for _ in range(N)]

    dict = {}

    for i in range(N): # 0 1 2 3 4 
        result = set()
        for j in range(len(student[i])):# 0 1 2 3 4
            for k in range(N): # 0 1 2 3 4
                if student[i][j] == student[k][j]: # student[0][0] -> [0~4]
                                                   # student[0][1] -> []
                    result.add(k)
        
        dict[i+1] = len(result)-1

    sorted_lst = sorted(dict.items(), key=lambda x: (x[1], -x[0]))
    
    x,y = sorted_lst[-1]
    print(x)
solve()
