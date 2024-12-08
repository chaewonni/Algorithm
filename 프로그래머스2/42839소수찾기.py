def solution(numbers):
    
    num_list = list(numbers)
    
    visited = [False] * len(num_list)

    def isPrime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    result = []
    answer = set()
    def dfs():
        for i, num in enumerate(num_list): # 0,1 1,7
            if not visited[i]:
                result.append(num)
                visited[i] = True
                check = int(''.join(result))
                if isPrime(check):
                    answer.add(check)
                dfs()
                visited[i] = False
                result.pop()
    
    dfs()
    print(answer)
    return len(answer)