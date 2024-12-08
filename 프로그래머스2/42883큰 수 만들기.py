def solution(number, k):
    answer = ''
    number = list(map(int, number))
    
    result = []
    cnt = 0
    
    for num in number:
        if not result:
            result.append(num)
        else:
            while result and result[-1] < num and cnt < k:
                result.pop()
                cnt += 1
            result.append(num)
    if result:
        while result and cnt != k:
            result.pop()
            cnt += 1

    answer = ''.join(map(str, result))
    return answer