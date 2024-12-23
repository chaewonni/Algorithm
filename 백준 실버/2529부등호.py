def solve():
    
    k = int(input())
    check = list(input().split())

    visited = [False] * 10
    cnt = []
    answer = []

    def dfs():
        if len(cnt) == k+1:
            answer.append(''.join(map(str, cnt)))
            return

        for i in range(0,10):
            if not visited[i]:
                if len(cnt) == 0 or (check[len(cnt)-1] == '<' and i > cnt[-1]) or (check[len(cnt)-1] == '>' and i < cnt[-1]):
                    visited[i] = True
                    cnt.append(i)
                    dfs()
                    cnt.pop()
                    visited[i] = False

    dfs()

    print(max(answer))
    print(min(answer))

solve()