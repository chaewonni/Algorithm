def solution(k, dungeons):
    answer = []
    visited = [False] * len(dungeons)
    result = []
    maxi = 0
    
    def dfs():
        nonlocal k
        nonlocal answer
        nonlocal maxi
        # print(result, len(result))
        if len(result) > maxi:
            maxi = len(result)
            # print(maxi)
        for i, dun in enumerate(dungeons):
            if not visited[i] and k >= dun[0]:
                visited[i] = True
                result.append(dun)
                k -= dun[1]
                dfs()
                visited[i] = False
                result.pop()
                k += dun[1]
        
    dfs()
    # print(maxi)
    return maxi